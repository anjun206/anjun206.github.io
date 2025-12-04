import os
import re

# Configuration
WIKI_DIR = 'wiki'
LEARN_DIR = os.path.join(WIKI_DIR, 'learn')

# Legacy mapping for 2024 (to preserve existing links)
LEGACY_2024_FILES = {
    '07': 'TILs.md',
    '08': 'TILs2.md',
    '09': 'TILs3.md',
    '10': 'TILs4.md',
    '11': 'TILs5.md',
    '12': 'TILs6.md',
    # If there were Jan-Jun 2024 files, we could map them too, but user started in July
}

MONTH_NAMES = {
    '01': '1월', '02': '2월', '03': '3월', '04': '4월', '05': '5월', '06': '6월',
    '07': '7월', '08': '8월', '09': '9월', '10': '10월', '11': '11월', '12': '12월'
}

def get_existing_titles(wiki_dir):
    titles = {}
    link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
    
    for filename in os.listdir(wiki_dir):
        if filename.startswith('TILs') and filename.endswith('.md'):
            path = os.path.join(wiki_dir, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = link_pattern.findall(content)
                    for title, link in matches:
                        if link.startswith('learn/'):
                            titles[link] = title
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return titles

def find_til_files(learn_dir):
    til_files = []
    # Regex to match TIL_MMDD or TIL_MMDD+...
    filename_pattern = re.compile(r'TIL_(\d{2})(\d{2})([+]*)\.md')
    
    for root, dirs, files in os.walk(learn_dir):
        for file in files:
            match = filename_pattern.match(file)
            if match:
                month, day, suffix = match.groups()
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, WIKI_DIR).replace('\\', '/')
                
                # Determine Year
                # Default to 2024
                year = '2024'
                
                # Check path for year indicators
                path_parts = rel_path.split('/')
                for part in path_parts:
                    # Match 4-digit year (20xx)
                    if re.match(r'^20\d{2}$', part):
                        year = part
                        break
                    # Optional: Match short year like 25_ (but be careful of false positives)
                    # For now, explicit 4-digit year folders are safest and clearest.
                
                til_files.append({
                    'year': year,
                    'month': month,
                    'day': day,
                    'suffix': suffix,
                    'path': rel_path,
                    'full_path': full_path,
                    'filename': file
                })
    return til_files

def get_title_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
    except:
        pass
    return None

def generate_content(year, month, files, existing_titles):
    lines = []
    
    # Sort files
    files.sort(key=lambda x: (int(x['day']), x['suffix']))
    
    current_day = None
    
    for file in files:
        day = file['day']
        path = file['path']
        suffix = file['suffix']
        
        # Determine title
        title = existing_titles.get(path)
        if not title:
            file_title = get_title_from_file(file['full_path'])
            if file_title:
                title = file_title
            else:
                if suffix:
                    title = f"{int(month)}월 {int(day)}일 DLC {len(suffix)}"
                else:
                    title = f"{int(month)}월 {int(day)}일 TIL"
        
        if day != current_day:
            lines.append("") 
            if not suffix:
                lines.append(f"[{title}]({path})")
            else:
                lines.append(f"[{title}]({path})")
            current_day = day
        else:
            lines.append(f"- [{title}]({path})")
            
    return "\n".join(lines).strip()

def get_output_filename(year, month):
    if year == '2024' and month in LEGACY_2024_FILES:
        return LEGACY_2024_FILES[month]
    else:
        return f"TILs_{year}_{month}.md"

def main():
    print("Scanning for existing titles...")
    existing_titles = get_existing_titles(WIKI_DIR)
    
    print("Scanning for TIL files...")
    til_files = find_til_files(LEARN_DIR)
    
    # Group by Year -> Month
    files_by_year_month = {}
    for file in til_files:
        y = file['year']
        m = file['month']
        if y not in files_by_year_month:
            files_by_year_month[y] = {}
        if m not in files_by_year_month[y]:
            files_by_year_month[y][m] = []
        files_by_year_month[y][m].append(file)
        
    all_years = sorted(files_by_year_month.keys())
    
    for year in all_years:
        months_in_year = sorted(files_by_year_month[year].keys())
        
        for month in months_in_year:
            filename = get_output_filename(year, month)
            print(f"Generating {filename} ({year}-{month})...")
            
            content = generate_content(year, month, files_by_year_month[year][month], existing_titles)
            
            # Navigation
            nav = []
            nav.append("<br>\n")
            
            # 1. Links to other months in the SAME year
            nav.append(f"### {year}년")
            for m in months_in_year:
                if m != month:
                    m_name = MONTH_NAMES.get(m, f"{m}월")
                    f_name = get_output_filename(year, m)
                    nav.append(f"- [{m_name}달로]({f_name})")
            
            # 2. Links to OTHER years
            other_years = [y for y in all_years if y != year]
            if other_years:
                nav.append("\n### 다른 연도")
                for y in other_years:
                    # Link to the first available month of that year
                    first_month = sorted(files_by_year_month[y].keys())[0]
                    f_name = get_output_filename(y, first_month)
                    nav.append(f"- [{y}년으로]({f_name})")

            full_content = content + "\n\n" + "\n".join(nav)
            
            # Preserve footer for TILs.md (July 2024)
            if filename == 'TILs.md':
                 full_content += "\n\n<br><br><br>\n\n# csapp\n\n[csapp로](csapp.md)"

            output_path = os.path.join(WIKI_DIR, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
                
    print("Done!")

if __name__ == "__main__":
    main()
