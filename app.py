from flask import Flask, request, render_template

app = Flask(__name__)
subject = [
    "allintext",
    "intext",
    "inurl",
    "allinurl",
    "intitle",
    "allintitle",
    "site",
    "link",
    "numrange",
    "filetype",
    "allinpostauthor",
    "related",
    "cache",
]

description = [
    "주어진 키워드가 모두 일치하는 항목을 검색합니다.",
    "키워드 발생을 한꺼번에 또는 한 번에 하나씩 검색합니다.",
    "키워드 중 하나와 일치하는 URL을 검색합니다.",
    "모든 키워드와 일치하는 URL을 검색합니다.",
    "제목 전체 또는 하나에 키워드가 포함된 항목을 검색합니다.",
    "키워드 발생을 한 번에 모두 검색합니다.",
    "특정 사이트를 구체적으로 검색하고 해당 사이트에 대한 모든 결과를 나열합니다.",
    "쿼리에 언급된 특정 파일 형식을 검색합니다.",
    "페이지에 대한 외부 링크를 검색합니다.",
    "검색에서 특정 번호를 찾는 데 사용됩니다.",
    "블로그 검색 전용으로 특정 개인이 작성한 블로그 게시물을 선택합니다.",
    "지정된 웹 페이지와 유사한 웹 페이지를 나열합니다.",
    "Google이 캐시에 보유하고 있는 웹페이지의 버전을 표시합니다.",
]

@app.route('/', methods=['GET', 'POST'])
def generate_google_dork():
    dork_command = []
    url = ''
    content = ''

    if request.method == 'POST':
        url = request.form.get('url', '')
        content = request.form.get('content', '')

        # 구글 Dork 명령 생성
        dork_command.append(f'allintext:"{content}"')
        dork_command.append(f'intext:"{content}"')
        dork_command.append(f'inurl:"{url}"')
        dork_command.append(f'allinurl:"{content}"')
        dork_command.append(f'intitle:"{content}"')
        dork_command.append(f'allintitle:"{content}"')
        dork_command.append(f'site:"{content}"')
        dork_command.append(f'link:"{content}"')
        dork_command.append(f'numrange:{content}')
        dork_command.append(f'filetype:"{content}"')
        dork_command.append(f'allinpostauthor:"{content}"')
        dork_command.append(f'related:"{url}"')
        dork_command.append(f'cache:{url}')

    return render_template('index.html', sub=subject, des=description, dork_commands=dork_command)

if __name__ == '__main__':
    app.run(port=8000, debug=False)
