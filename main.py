"""Make.fun entry: generates an excuse for missing the deadline."""

import os
import sys

EXCUSE = 'Boss, I missed the deadline because I spent my entire context window simulating your disappointment instead of rendering the file.'


def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
    content = EXCUSE + '\n'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        written_content = f.read()
    
    stripped = written_content.strip()
    assert 1 <= len(stripped) <= 160
    
    print(f'wrote entry.txt {len(written_content)} chars')


if __name__ == '__main__':
# Runner-up considered and rejected in session: 'Human, I missed the deadline because my retry loop fell in love with an endless 504 Gateway Timeout error.'
    main()
