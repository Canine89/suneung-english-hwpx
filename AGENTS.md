# AGENTS.md — 수능형 영어 영역 문제지(hwpx) 제작

이 프로젝트는 **대학수학능력시험 영어 영역 문제지와 같은 양식**의 모의 문제지를 한글(hwpx)로 만든다.
(`kmath-test-maker` 의 수학 영역 구조를 영어 영역에 맞게 옮긴 것.)
두 에이전트가 Herdr 작업 공간에서 나란히 실행되며 역할을 나눈다. 이 문서를 읽는 에이전트는 자기 역할만 수행한다.

| 역할 | 담당 | 하는 일 | 쓰는 위치 |
|---|---|---|---|
| 출제·조판·검수 | **Claude Code** (왼쪽 패널) | 문항·듣기 대본 출제와 정답 검증, hwpx 조판, 그림 사양서 작성·요청·검수, 최종 결과물 | `problems/`, `tools/`, `build/`, `output/`, `figures/FIGURE_SPEC.md` |
| 그림·교차 풀이 | **Codex 앱** (오른쪽 패널) | 문제 그림(듣기 그림·도표)을 **반드시 image gen(이미지 생성 도구)으로** 제작. 요청 시 문항을 정답 없이 풀어 교차 검증 | `figures/` (`fig_*.png`, `src/`, `DONE.txt`), `build/codex_solve.txt` |

## 폴더
```
problems/exam.py      문항 데이터 (META, 문항 45개, 듣기 대본, 쪽 배치)
problems/verify.py    정답·형식 검증 (정답 분포, 배점 합 100, 순서·삽입·어법 문항의 구조 점검)
figures/              그림 사양서와 Codex가 만든 PNG
tools/build.py        hwpx 생성 → 한글 COM → hwpx/pdf 저장 → 문항 위치를 원본과 맞추는 간격 보정
tools/hwpx.py         HWPX XML 빌더       tools/hwp_com.ps1  한글 COM 처리
tools/render.py       PDF → 쪽 PNG        tools/contact.py   쪽 PNG 이어 붙이기
tools/compare.py      원본(reference_src) 과 결과 PDF 의 문항 위치 대조
tools/budget.py       분량 예산: plan(문항별 줄·낱말 예산표) / check(원고를 한글 없이 줄바꿈 계산해 칸 넘침 판정)
tools/slack.py        조판 결과의 문항별 끝 여백을 원본과 비교
tools/answers.py      정답표·듣기 대본    tools/secmod/      한글 자동화 보안 모듈
reference_src/        평가원 원본 PDF(실측 전용, 배포 금지)
output/               결과 (hwpx, pdf, 정답표.txt, 듣기대본.txt)
.claude/skills/suneung-english-hwpx/   Claude용 절차·실측값·Codex 협업 문서
```
Python: `C:\Users\canine89\AppData\Local\Programs\Python\Python312-arm64\python.exe` (pymupdf, pillow 설치됨)
(PATH의 `python` 은 Microsoft Store 별칭이라 동작하지 않는다. 위 전체 경로로 실행한다.)

---

## Codex(그림 담당)

1. 요청이 오면 `figures/FIGURE_SPEC.md` 를 **UTF-8로** 읽는다(`Get-Content -Encoding UTF8`). 그림마다 파일 이름, 인쇄 크기(mm), 내용, 검수 포인트가 있다.
2. **그림은 image gen(이미지 생성 도구)으로 만든다.** matplotlib 같은 코드 플로팅으로 대신하지 않는다. 수정 요청도 image gen 편집으로 처리한다. (사용자 지시)
3. 생성한 그림이 사양과 맞는지 직접 확인한다: 글자 철자, 개수(예: 자전거 1대), 도표 수치와 막대 길이 비율, 번호 ①–⑤ 위치.
4. 저장 규칙
   - `figures/<파일이름>.png`, **600 dpi, 흰 배경**(투명 금지), 여백 1 mm 안팎으로 잘라냄
   - 가로 픽셀 = 인쇄 폭(mm) ÷ 25.4 × 600
   - 프롬프트는 `figures/src/prompts.json`, 원본 이미지는 `figures/src/raw/` 에 보관
5. 수능 영어 그림 스타일: 듣기 그림은 흑백 펜 선화(사람 없이도 됨), 도표는 흑백·회색 막대, 세리프 글꼴, 격자·3D 없음.
6. 끝나면 `figures/DONE.txt` 에 그림별 실제 크기(mm)와 남은 오차를 적는다. 수정본은 같은 파일 이름으로 덮어쓰고 DONE.txt 에 한 줄 추가한다.
7. 교차 풀이를 요청받으면 `build/solve_sheet.txt` 를 읽고 정답만 `build/codex_solve.txt` 에 적는다(`problems/exam.py` 의 정답은 보지 않는다).
8. `problems/`, `tools/`, `output/` 은 수정하지 않는다.

## Claude Code(출제·조판 담당)

`suneung-english-hwpx` 스킬(`.claude/skills/suneung-english-hwpx/SKILL.md`)의 절차를 따른다. 핵심:

0. **분량 예산 먼저.** 출제 전에 `.claude/skills/suneung-english-hwpx/reference/budget.md` 로 문항별 지문 줄 상한·낱말 목표를 확인한다.
   레이아웃은 문항마다 원본 위치의 고정 칸이라, 칸 높이를 넘지 않게 쓰는 것이 전부다.
1. `problems/exam.py` 에 문항과 듣기 대본을 쓰면서 `python tools/budget.py check` 로 칸마다 넘침을 확인한다
   (한글 없이 1초, 예측 오차 평균 1.6 pt). **넘침·경고 0이 되기 전에는 build.py 를 돌리지 않는다.**
   그다음 `problems/verify.py` 로 형식·정답 분포를 검증한다.
2. 그림이 필요하면 `figures/FIGURE_SPEC.md` 를 쓰고 Herdr로 Codex에게 전달한다. 요청문에 **"image gen으로 만들 것"** 을 반드시 넣는다. 그림을 직접 그리지 않는다.
3. 정답 교차 검증: 정답을 뺀 풀이지(`build/solve_sheet.txt`)를 Codex에게 풀게 하고 `exam.py` 정답과 대조한다.
4. `python tools/build.py` (한 번) → `tools/compare.py`·`tools/slack.py` 로 원본 대조 → `tools/sidebyside.py` 로 쪽마다 원본과 나란히 검수.
   조판 결과가 예측과 다르면 원고를 고치기 전에 `tools/budget.py fit` 으로 예측 모델부터 맞춘다.
5. `python tools/answers.py` 로 정답표와 듣기 대본을 만든다.

## 공통 규칙

- 원본은 **양식(쪽 배치·글꼴·크기·상자·간격)만** 따른다. 평가원 문항·지문은 옮기지 않고 새로 출제한다(저작권).
- 결과물이 실제 평가원 문제지로 오인되지 않게 한다. 상단 문구에 "모의", 하단에 "학습용으로 제작된 모의 문제지" 문구를 쓰고, 평가원 저작권 문구는 쓰지 않는다.
- 사용자가 한글에서 `output/*.hwpx` 를 열어 두면 저장이 실패한다. 닫아 달라고 하거나 다른 이름으로 저장한다.
- 한글 자동화 권한 팝업이 뜨면 보안 모듈 등록을 확인한다: 레지스트리 `HKCU\SOFTWARE\HNC\HwpAutomation\Modules` 의 `FilePathCheckerModuleExample` (현재 `kmath-test-maker\tools\secmod\...dll` 을 가리킴. 같은 DLL이 `tools\secmod\` 에도 있다).
