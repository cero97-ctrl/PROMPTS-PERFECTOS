import os
import re

# Configuración de directorios
SOURCE_DIR = 'ejemplos'
DEST_DIR = 'docs'

# Plantilla del preámbulo LaTeX
LATEX_PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{array}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{hyperref}

\lstset{
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
    backgroundcolor=\color{gray!10},
    extendedchars=true,
    literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1 {ñ}{{\~n}}1
}
"""

def parse_markdown(content):
    lines = content.split('\n')
    tex_lines = []
    
    # Extracción del título (primer H1)
    title = "Documento Generado"
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
            
    tex_lines.append(LATEX_PREAMBLE)
    tex_lines.append(f'\\title{{{title}}}')
    tex_lines.append(r'\author{Gemini Code Assist}')
    tex_lines.append(r'\date{\today}')
    tex_lines.append(r'\begin{document}')
    tex_lines.append(r'\maketitle')
    tex_lines.append('')

    state = 'normal' # normal, code, table, itemize, enumerate
    
    for line in lines:
        stripped = line.strip()
        
        # Ignorar el título principal ya que se usa en \maketitle
        if line.startswith('# ') and title in line:
            continue

        # --- Bloques de Código ---
        if stripped.startswith('```'):
            if state == 'code':
                tex_lines.append(r'\end{lstlisting}')
                state = 'normal'
            else:
                # Cerrar otros estados
                if state == 'itemize': tex_lines.append(r'\end{itemize}'); state = 'normal'
                if state == 'enumerate': tex_lines.append(r'\end{enumerate}'); state = 'normal'
                if state == 'table': tex_lines.append(r'\end{tabular}'); tex_lines.append(r'\end{table}'); state = 'normal'
                
                tex_lines.append(r'\begin{lstlisting}')
                state = 'code'
            continue
            
        if state == 'code':
            tex_lines.append(line)
            continue

        # --- Tablas ---
        if stripped.startswith('|'):
            if state != 'table':
                if state == 'itemize': tex_lines.append(r'\end{itemize}'); state = 'normal'
                if state == 'enumerate': tex_lines.append(r'\end{enumerate}'); state = 'normal'
                
                tex_lines.append(r'\begin{table}[h]')
                tex_lines.append(r'\centering')
                tex_lines.append(r'\renewcommand{\arraystretch}{1.5}')
                
                # Calcular columnas
                cols = line.count('|') - 1
                if cols < 1: cols = 1
                width = 0.9 / cols
                col_spec = '|' + '|'.join([f'p{{{width:.2f}\\textwidth}}' for _ in range(cols)]) + '|'
                
                tex_lines.append(f'\\begin{{tabular}}{{{col_spec}}}')
                tex_lines.append(r'\hline')
                state = 'table'
            
            # Procesar fila
            row_content = stripped.strip('|')
            # Detectar separador (---)
            if set(row_content.replace('|', '').replace('-', '').replace(':', '').strip()) == set():
                continue
                
            cells = row_content.split('|')
            formatted_cells = []
            for cell in cells:
                c = cell.strip()
                c = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', c)
                c = re.sub(r'\*(.*?)\*', r'\\textit{\1}', c)
                c = c.replace('<br>', r' \newline ')
                formatted_cells.append(c)
            
            tex_lines.append(' & '.join(formatted_cells) + r' \\')
            tex_lines.append(r'\hline')
            continue
            
        elif state == 'table':
            tex_lines.append(r'\end{tabular}')
            tex_lines.append(r'\end{table}')
            state = 'normal'

        # --- Listas ---
        # No ordenadas
        if stripped.startswith('- ') or stripped.startswith('* '):
            if state != 'itemize':
                if state == 'enumerate': tex_lines.append(r'\end{enumerate}')
                tex_lines.append(r'\begin{itemize}')
                state = 'itemize'
            
            content = stripped[2:]
            content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', content)
            tex_lines.append(f'    \\item {content}')
            continue
            
        # Ordenadas
        if re.match(r'^\d+\.', stripped):
            if state != 'enumerate':
                if state == 'itemize': tex_lines.append(r'\end{itemize}')
                tex_lines.append(r'\begin{enumerate}')
                state = 'enumerate'
            
            content = re.sub(r'^\d+\.\s*', '', stripped)
            content = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', content)
            tex_lines.append(f'    \\item {content}')
            continue
            
        # Cerrar listas si la línea no es lista y no está vacía
        if state in ['itemize', 'enumerate'] and stripped:
            if state == 'itemize': tex_lines.append(r'\end{itemize}')
            if state == 'enumerate': tex_lines.append(r'\end{enumerate}')
            state = 'normal'

        # --- Encabezados ---
        if line.startswith('#'):
            if state == 'itemize': tex_lines.append(r'\end{itemize}'); state = 'normal'
            if state == 'enumerate': tex_lines.append(r'\end{enumerate}'); state = 'normal'
            
            if line.startswith('### '):
                tex_lines.append(f'\\subsection{{{line[4:].strip()}}}')
            elif line.startswith('## '):
                tex_lines.append(f'\\section{{{line[3:].strip()}}}')
            continue

        # --- Separadores ---
        if stripped == '---':
            tex_lines.append(r'\vspace{0.5cm}')
            continue

        # --- Texto Normal ---
        if not stripped:
            tex_lines.append('')
            continue
            
        text = line
        text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
        text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
        
        tex_lines.append(text + r' \\')

    # Cerrar estados pendientes al final
    if state == 'itemize': tex_lines.append(r'\end{itemize}')
    if state == 'enumerate': tex_lines.append(r'\end{enumerate}')
    if state == 'table': tex_lines.append(r'\end{tabular}'); tex_lines.append(r'\end{table}')
    
    tex_lines.append(r'\end{document}')
    return '\n'.join(tex_lines)

def main():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        print(f"Directorio creado: {DEST_DIR}")

    if not os.path.exists(SOURCE_DIR):
        print(f"Error: El directorio {SOURCE_DIR} no existe.")
        return

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.md'):
            src_path = os.path.join(SOURCE_DIR, filename)
            dest_filename = filename.replace('.md', '.tex')
            dest_path = os.path.join(DEST_DIR, dest_filename)
            
            print(f"Procesando: {filename} -> {dest_filename}")
            
            try:
                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                tex_content = parse_markdown(content)
                
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(tex_content)
            except Exception as e:
                print(f"Error convirtiendo {filename}: {e}")

    print("Proceso finalizado.")

if __name__ == "__main__":
    main()