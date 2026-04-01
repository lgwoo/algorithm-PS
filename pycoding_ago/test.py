import os
import re

# 작업할 폴더 경로 (현재 폴더면 '.' 사용)
folder_path = 'D:\\doctorWHO\\[미드] 닥터 후 시즌 2 Doctor.Who.2006.S02.13부작완결.720p.한글자막'

for filename in os.listdir(folder_path):
    # S02E02 같은 패턴 찾기
    match = re.search(r'(S\d{2}E\d{2})', filename)
    
    if match:
        episode = match.group(1)
        
        # 확장자 유지
        ext = os.path.splitext(filename)[1]
        
        new_name = episode + ext
        
        # 전체 경로
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # 이름 변경
        os.rename(old_file, new_file)
        
        print(f'{filename} -> {new_name}')