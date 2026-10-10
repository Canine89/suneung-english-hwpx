# suneung-english-hwpx

대학수학능력시험 **영어 영역 문제지와 같은 양식**의 모의 문제지를 한글(hwpx)로 만드는
Claude Code 스킬과 에이전트 협업 규칙(AGENTS.md)입니다.

- `AGENTS.md` — Herdr 작업 공간에서 Claude Code(출제·조판·검수)와 Codex(그림 image gen·교차 풀이)의 역할 분담
- `.claude/skills/suneung-english-hwpx/SKILL.md` — 출제 → 분량 예산 점검 → 검증 → 조판 → 검수 절차
- `reference/layout-spec.md` — 2026학년도 수능 영어 홀수형 실측값(쪽 배치, 글꼴·크기·장평, 줄 피치, 상자)
- `reference/budget.md` — 문항별 분량 예산(칸 높이, 원본 구성, 지문 줄 상한·낱말 목표)
- `reference/codex-figures.md` — Herdr로 Codex에 그림·교차 풀이를 맡기는 방법
- `templates/FIGURE_SPEC_example.md` — 듣기 그림·도표 사양서 예시
- `samples/` — 이 스킬로 만든 모의 문제지 2회분(pdf·hwpx, 정답표, 듣기 대본, 원고 `exam.py`, 그림과 프롬프트).
  처음 보는 분은 `samples/2027-모의2/output/영어영역_문제지.pdf` 부터 열어 보세요. 자세한 설명은 `samples/README.md`.

## 참고
- 스킬이 부르는 `tools/`(build.py, budget.py 등)와 `problems/` 는 이 레포에 포함되어 있지 않습니다.
- 평가원 원본 문제지 PDF는 저작권 때문에 포함하지 않습니다. 원본은 **양식 실측에만** 쓰고, 문항은 새로 출제합니다.
- 만든 문제지에는 "모의" 문구와 "학습용으로 제작된 모의 문제지" 문구를 넣고 평가원 저작권 문구는 쓰지 않습니다.
