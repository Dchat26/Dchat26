import os

# [설정]
백준_경로 = "C:/doit/github/Baekjoon/백준"
프로_경로 = "C:/doit/github/Programmers/프로그래머스/lv0"

Fcount = 2         # 폴더 내 최소 파일 개수 기준
Fpath = 프로_경로    # 현재 검사 대상

def print_baekjoon_summary(root_path):
    """백준 전역 분류별 폴더 개수 요약"""
    target_folders = ['Gold', 'Silver', 'Bronze']
    print("\n📊 [백준 티어별 요약]")
    
    for target in target_folders:
        folder_path = os.path.join(root_path, target)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            sub_dirs = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
            print(f" - {target:6}: {len(sub_dirs)}개 문제")
        else:
            print(f" - {target:6}: 폴더 없음")
    print("-" * 35)

def check_recursive(root_path):
    """모든 최하위 폴더의 전체 파일 개수 검사"""
    if "백준" in root_path:
        print_baekjoon_summary(root_path)
        
    default_ignore = {".git", ".vscode", "__pycache__"}
    ignore_list = {"18110"} 
    
    total_folders = 0
    error_folders = 0
    
    print(f"\n🔍 [개수 미달 검사] 기준: 전체 파일 {Fcount}개 미만\n")
    
    for root, dirs, files in os.walk(root_path):
        # 제외 폴더 가지치기
        dirs[:] = [d for d in dirs if d not in default_ignore and not any(key in d for key in ignore_list)]
        
        # 최하위 문제 폴더(dirs가 비어있는 곳)만 검사
        if not dirs and root != root_path:
            total_folders += 1
            
            # 파일 형식 상관없이 전체 파일 개수
            file_sum = len(files)
            
            if file_sum < Fcount:
                rel_path = os.path.relpath(root, root_path)
                error_folders += 1
                print(f"⚠️ [개수 미달] {rel_path} (현재 {file_sum}개)")
                
    # 최종 결과 요약
    print("\n" + "="*45)
    print(f"📁 총 문제 폴더 개수 : {total_folders}개")
    print(f"✅ 정상 관리 폴더    : {total_folders - error_folders}개")
    print(f"❌ 개수 미달 폴더    : {error_folders}개")
    print("="*45)

if __name__ == "__main__":
    check_recursive(Fpath)
