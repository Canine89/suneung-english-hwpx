"""영어 영역 모의 문제지 문항 데이터 (2026학년도 수능 영어 홀수형 양식).

표기 규칙
- 문자열 안 서식 태그: <u>밑줄</u>, <i>기울임</i>, <b>굵게</b>, <blank> (빈칸 밑줄), <blank:n> (n칸 빈칸),
  <ublank:(A)> (가운데 (A) 가 들어간 요약문 빈칸).
- 블록
  ('q', 발문)                       한국어 발문(영어 낱말은 자동으로 Times New Roman)
  ('p', 지문) / ('p0', 지문)         영어 지문 문단 (p: 첫 줄 들여쓰기, p0: 들여쓰기 없음)
  ('fn', 각주)                      오른쪽 정렬 각주 ("* a: 뜻   ** b: 뜻")
  ('ch', [보기 5개], 단수)           단수 1, 2, 3, 5
  ('emo', [(a, b) x5])              심경 변화 보기 (a → b), 2단
  ('ord', [보기 5개])               순서 배열 보기, 2단
  ('ab', [(a, b) x5])               요약문 (A)(B) 보기, 2단
  ('speaker', 'Man:')               응답 문항의 화자 + 밑줄
  ('fig', 파일이름, 가로pt, 세로pt)
  ('tbl10', 제목, 머리행, 행들)      듣기 10번 표
  ('notice', 제목, 줄들)            27·28번 안내문 상자
  ('letter', 문단들)                18번 편지 상자
  ('box', [블록...])                들여 쓴 상자(주어진 글·요약 지문 등)
  ('arrow',)                        요약문 화살표
  ('summary', 문장)                 요약문 상자
- 'ans' 는 정답 번호, 'pts' 는 배점. 'script' 는 듣기 대본 [(화자, 대사)].
"""

META = {
    "year_title": "2027학년도 대학수학능력시험 모의 문제지",
    "period": "제 3 교시",
    "type": "홀수형",
    "subject": "영어 영역",
    "copyright": "이 문제지는 학습용으로 제작된 모의 문제지입니다.",
    "out_name": "영어영역_문제지",
}

LISTEN_NOTICE = ("1번부터 17번까지는 듣고 답하는 문제입니다. 1번부터 15번까지는 한 번만 들려주고, "
                 "16번부터 17번까지는 두 번 들려줍니다. 방송을 잘 듣고 답을 하시기 바랍니다.")
LISTEN_END = "이제 듣기 문제가 끝났습니다. 18번부터는 문제지의 지시에 따라 답을 하시기 바랍니다."

ORD3 = ["(A) － (C) － (B)", "(B) － (A) － (C)", "(B) － (C) － (A)", "(C) － (A) － (B)", "(C) － (B) － (A)"]
ORD4 = ["(B) － (D) － (C)", "(C) － (B) － (D)", "(C) － (D) － (B)", "(D) － (B) － (C)", "(D) － (C) － (B)"]
ABCDE = ["(a)", "(b)", "(c)", "(d)", "(e)"]

Q = {}


def q(no, pts, ans, blocks, script=None):
    Q[no] = dict(no=no, pts=pts, ans=ans, blocks=blocks, script=script or [])


# =============================================================== 듣기 1–17
q(1, 2, 3, [
    ('q', "다음을 듣고, 여자가 하는 말의 목적으로 가장 적절한 것을 고르시오."),
    ('ch', ["학교 체육관 보수 공사 일정을 안내하려고",
            "교내 분실물 보관 장소 변경을 공지하려고",
            "교내 텀블러 사용 캠페인 참여를 독려하려고",
            "급식실 운영 시간 변경을 알리려고",
            "환경 동아리 신규 회원 모집을 홍보하려고"], 1)],
    [("W", "Good morning, students. This is Ms. Carter from the student council's environment committee. Every "
           "day, our school throws away more than five hundred paper cups. To reduce this waste, we're starting "
           "the Bring Your Own Tumbler campaign next Monday. Please bring your own tumbler or reusable bottle to "
           "school. You can fill it with water at any of the new water stations in the cafeteria and the "
           "library. Each time you use your tumbler at the school store, you'll get a stamp on your campaign "
           "card. Students who collect ten stamps will receive a small eco-friendly gift. Small actions can "
           "make a big difference, so please join us and help make our school greener. Thank you.")])

q(2, 2, 5, [
    ('q', "대화를 듣고, 남자의 의견으로 가장 적절한 것을 고르시오."),
    ('ch', ["여행지는 계절을 고려하여 선택해야 한다.",
            "여행 일정은 여유 있게 계획하는 것이 좋다.",
            "해외여행을 갈 때는 여행자 보험에 가입해야 한다.",
            "현지 음식을 먹어 보는 것이 여행의 큰 즐거움이다.",
            "여행 전에 현지어 인사말을 익혀 두는 것이 좋다."], 1)],
    [("W", "Dad, I've finished packing for my trip to Spain. I think I'm ready."),
     ("M", "Great, Sarah. By the way, have you learned any Spanish?"),
     ("W", "Not really. Most people there speak some English, don't they?"),
     ("M", "Many do, but I think it's worth learning a few basic greetings before you go."),
     ("W", "Why? I'll only be there for a week."),
     ("M", "Even simple words like hello, please, and thank you make a big difference. Local people really "
           "appreciate the effort."),
     ("W", "Hmm, I guess that could make conversations friendlier."),
     ("M", "Exactly. When I traveled to Italy, saying good morning in Italian made shop owners smile and "
           "help me more."),
     ("W", "That sounds nice. Maybe I should download a language app."),
     ("M", "Good idea. Learning a few local greetings before a trip is always a good investment.")])

q(3, 2, 1, [
    ('q', "다음을 듣고, 여자가 하는 말의 요지로 가장 적절한 것을 고르시오.", {"sp": -12}),
    ('ch', ["작은 목표를 세우면 큰 과제를 끝까지 해낼 수 있다.",
            "계획을 자주 바꾸면 일의 효율이 떨어진다.",
            "다른 사람과 목표를 공유하면 동기가 높아진다.",
            "충분한 휴식은 집중력 회복에 도움이 된다.",
            "마감 기한을 정하면 미루는 습관을 고칠 수 있다."], 1)],
    [("W", "Hello, everyone. Welcome to Study Smart. Have you ever stared at a huge project and felt so "
           "overwhelmed that you didn't know where to start? Many students give up before they even begin "
           "because the task seems too big. Here's my advice. Break the project into small, specific goals. "
           "Instead of saying, 'I'll write my research paper this week,' say, 'Today, I'll find three sources,' "
           "and 'Tomorrow, I'll write the introduction.' Each small goal is easy to reach, and finishing it "
           "gives you a sense of achievement that keeps you going. Step by step, the big project gets done. "
           "So the next time a task feels impossible, remember that small goals can carry you all the way to "
           "the finish line.")])

q(4, 2, 2, [
    ('q', "대화를 듣고, 그림에서 대화의 내용과 일치하지 <u>않는</u> 것을 고르시오.", {"sp": -10}),
    ('fig', "fig_l04", 306.2, 187.2)],
    [("M", "Emily, is this the picture of your science fair booth?"),
     ("W", "Yes, Dad. We finished setting it up this afternoon. What do you think?"),
     ("M", "It looks great. I like the banner that says SCIENCE FAIR at the top."),
     ("W", "Thanks. Our art club helped us make it."),
     ("M", "And you covered the table with a flower-patterned tablecloth. It looks bright."),
     ("W", "Right. My mom lent it to us."),
     ("M", "I see a volcano model on the table. Is that your project?"),
     ("W", "Yes. It actually erupts with baking soda and vinegar."),
     ("M", "Cool. And there are two potted plants under the table."),
     ("W", "We put them there to make the booth look more natural."),
     ("M", "Nice touch. Oh, there's a poster of the solar system on the wall behind the booth."),
     ("W", "That's from the astronomy club next to us. We're sharing the wall.")])

q(5, 2, 4, [
    ('q', "대화를 듣고, 남자가 할 일로 가장 적절한 것을 고르시오."),
    ('ch', ["장보기", "텐트 빌리기", "지도 출력하기", "버스 예약하기", "사진기 충전하기"], 2)],
    [("W", "Tony, our club's camping trip is this Saturday. Let's check what's left to do."),
     ("M", "Sure. I already bought the food yesterday, so we don't need to go shopping."),
     ("W", "Great. What about the tents?"),
     ("M", "Kate borrowed two tents from the sports center."),
     ("W", "Perfect. And I printed the trail maps this morning."),
     ("M", "Good. Did anyone charge the camera?"),
     ("W", "Jason said he'd do it tonight. But how are we getting to the campsite?"),
     ("M", "Oh, no. We still haven't booked the bus."),
     ("W", "We'd better hurry. Seats might sell out."),
     ("M", "Don't worry. I'll book the bus online right now.")])

q(6, 2, 3, [
    ('q', "대화를 듣고, 여자가 지불할 금액을 고르시오."),
    ('ch', ["$36", "$40", "$45", "$50", "$54"], 5)],
    [("M", "Welcome to Bloom Flower Shop. How can I help you?"),
     ("W", "Hi. I'd like some roses for my mother's birthday. How much are they?"),
     ("M", "They're $3 each."),
     ("W", "I'll take ten roses, please."),
     ("M", "Okay. Would you like a vase as well? This glass one is $20."),
     ("W", "It's beautiful. I'll take it."),
     ("M", "So that's ten roses and one vase. Do you need delivery?"),
     ("W", "No, I'll take them with me. Oh, I have this membership card. Can I get a discount?"),
     ("M", "Yes. Members get 10% off the total price."),
     ("W", "Great. Here's my card.")])

q(7, 2, 1, [
    ('q', "대화를 듣고, 남자가 수영 강습에 갈 수 <u>없는</u> 이유를 고르시오."),
    ('ch', ["감기에 걸려서", "수영복을 잃어버려서", "아르바이트를 해야 해서",
            "강습이 취소되어서", "친구 생일 파티에 가야 해서"], 1, 149)],
    [("W", "Hi, Mark. Are you coming to swimming class this evening?"),
     ("M", "I'm afraid not, Jenny."),
     ("W", "Why not? Did you lose your swimsuit again?"),
     ("M", "No, I found it in my locker."),
     ("W", "Then do you have to work at the bookstore tonight?"),
     ("M", "No, I don't work on Wednesdays."),
     ("W", "Hmm. The class wasn't canceled, was it?"),
     ("M", "No, it's still on. Actually, I caught a cold, and the doctor told me to rest for a few days."),
     ("W", "Oh, I'm sorry to hear that. I hope you feel better soon."),
     ("M", "Thanks. I'll see you at next week's class.")])

q(8, 2, 5, [
    ('q', "대화를 듣고, Greenfield Book Fair에 관해 언급되지 <u>않은</u> 것을 고르시오."),
    ('ch', ["개최 장소", "기간", "입장료", "참여 작가", "주차 요금"], 3)],
    [("M", "Lisa, have you heard about the Greenfield Book Fair?"),
     ("W", "No. What is it?"),
     ("M", "It's a book fair held at the Greenfield Convention Center."),
     ("W", "Sounds fun. When is it?"),
     ("M", "It runs for three days, from May 12th to the 14th."),
     ("W", "Do we have to pay to get in?"),
     ("M", "No. Admission is free for everyone."),
     ("W", "Great. Will any authors be there?"),
     ("M", "Yes. Over twenty authors, including Ryan Brooks, will sign books and give talks."),
     ("W", "Really? I love his novels. Let's go together.")])

q(9, 2, 2, [
    ('q', "2027 City Marathon for Charity에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오."),
    ('ch', ["10월 첫째 주 일요일에 열린다.",
            "참가자는 모두 10킬로미터를 달린다.",
            "참가비는 어린이 병원에 기부된다.",
            "완주자 전원에게 메달을 준다.",
            "9월 20일까지 온라인으로 신청해야 한다."], 1, 149)],
    [("M", "Hello, listeners. I'm Brian Hall from the city sports office. I'm excited to announce the 2027 City "
           "Marathon for Charity. The event will be held on the first Sunday of October, starting at Central "
           "Park. Runners can choose between two courses: a five-kilometer course and a ten-kilometer course. "
           "The participation fee is $30, and all of the money will be donated to the city's children's "
           "hospital. Every runner who finishes the race will receive a medal, and the top three runners in "
           "each course will get special prizes. To join the marathon, please sign up on our website by "
           "September 20th. Run for your health, and run for the children!")])

q(10, 2, 4, [
    ('q', "다음 표를 보면서 대화를 듣고, 남자가 구입할 책상 스탠드를 고르시오."),
    ('tbl10', "Desk Lamps",
     ["Model", "Price", "Brightness|Levels", "Color", "USB|Port"],
     [["A", "$22", "3", "White", "×"],
      ["B", "$28", "5", "Black", "○"],
      ["C", "$34", "3", "Black", "○"],
      ["D", "$39", "5", "White", "○"],
      ["E", "$47", "7", "Black", "○"]])],
    [("W", "Kevin, what are you looking at?"),
     ("M", "I'm shopping for a desk lamp, Mom. Can you help me choose one?"),
     ("W", "Sure. How much do you want to spend?"),
     ("M", "No more than $45."),
     ("W", "Then this one is too expensive. What about brightness?"),
     ("M", "I want to adjust it a lot, so it should have at least five brightness levels."),
     ("W", "Okay. Then you have two choices left. Do you need a USB port?"),
     ("M", "Yes, I'd like to charge my phone while I study. Both of them have one."),
     ("W", "Then what about the color?"),
     ("M", "My desk is white, so I'll choose the white one."),
     ("W", "Good choice.")])

q(11, 2, 2, [
    ('q', "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오."),
    ('ch', ["Sorry, but I'm too busy to drive you to school.",
            "Hold on. Yes, it's right here next to your bowl.",
            "Don't worry. Your science test was postponed.",
            "Great. I'll buy you a new notebook tomorrow.",
            "Really? I thought you liked science class."], 1, 149)],
    [("W", "Hello, Jake. Why are you calling? Aren't you in class?"),
     ("M", "Mom, I think I left my science notebook on the kitchen table. Could you check if it's there?"),
     ("W", "")])

q(12, 3, 4, [
    ('q', "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]"),
    ('ch', ["Sure. I already bought popcorn for both of us.",
            "I'm sorry, but I don't like action movies.",
            "Okay. The theater is closed on weekends.",
            "Then let's watch the nine o'clock show instead.",
            "Don't worry. The traffic usually clears by noon."], 1, 149)],
    [("M", "Hello, Amy. Where are you? The movie starts in twenty minutes."),
     ("W", "Sorry, Jake. The traffic is terrible, and I don't think I'll get there by seven."),
     ("M", "")])

q(13, 3, 5, [
    ('q', "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]"),
    ('speaker', "Man:"),
    ('ch', ["Sorry, we don't accept returns without a receipt.",
            "I'm afraid this jacket is no longer on sale.",
            "You can try it on in the fitting room over there.",
            "The blue color looks really great on you.",
            "Of course. Just leave your phone number with us."], 1)],
    [("M", "Good afternoon. How can I help you?"),
     ("W", "Hi. I bought this jacket here last week, but it's too small for me."),
     ("M", "I see. Would you like to exchange it for a larger size?"),
     ("W", "Yes, please. I'd like the same jacket in a medium."),
     ("M", "Let me check. Hmm, we have a medium in black, but not in blue."),
     ("W", "Oh, I really wanted the blue one."),
     ("M", "We're expecting a new shipment next week. It should include the blue jacket in a medium."),
     ("W", "That's good news. I'll wait for it, then."),
     ("M", "All right. I'll keep your receipt on file."),
     ("W", "Thanks. Then could you let me know when the blue one comes in?"),
     ("M", "")])

q(14, 3, 3, [
    ('q', "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]"),
    ('speaker', "Woman:"),
    ('ch', ["No thanks. I don't have time to read books.",
            "Right. The library closes early on Fridays.",
            "Sure. I'll make a draft and show you tomorrow.",
            "Too bad. Nobody signed up for the club.",
            "Sorry. I already returned the book you lent me."], 1)],
    [("M", "Rachel, do you have a minute?"),
     ("W", "Sure, Steve. What's up?"),
     ("M", "I'm thinking of starting a reading club here at the office."),
     ("W", "That's a great idea. How would it work?"),
     ("M", "We'd read one book a month and meet during lunch on the last Friday to talk about it."),
     ("W", "Sounds fun. I've wanted to read more, but I never find the time."),
     ("M", "Me, too. That's why I think a club will help. Would you like to join?"),
     ("W", "Definitely. How will you tell everyone about it?"),
     ("M", "I'm planning to put up a poster in the break room. You're good at design, right?"),
     ("W", "Well, I did take a design class last year."),
     ("M", "Perfect. Would you help me design the poster for it?"),
     ("W", "")])

q(15, 2, 1, [
    ('q', "다음 상황 설명을 듣고, Daniel이 Sophie에게 할 말로 가장 적절한 것을 고르시오."),
    ('speaker', "Daniel:"),
    ('ch', ["Why don't you practice without looking at your script?",
            "Let's choose a different topic for your speech.",
            "You should sign up for the contest as early as possible.",
            "I think you need to speak a little more quickly.",
            "How about printing your speech in a larger font?"], 1)],
    [("W", "Sophie is going to take part in the school speech contest next week. She has written a great speech "
           "and practices it every day. Today, she asks her classmate Daniel to watch her practice. While she "
           "speaks, Daniel notices that Sophie reads every word from her paper and hardly ever looks up at the "
           "audience. He thinks her speech would be much more powerful if she made eye contact with the "
           "listeners. He also believes she knows the speech well enough to deliver it without the paper. So "
           "Daniel wants to suggest that Sophie practice her speech without her script. In this situation, "
           "what would Daniel most likely say to Sophie?")])

q(16, 2, 4, [
    ('q', "여자가 하는 말의 주제로 가장 적절한 것은?"),
    ('ch', ["why paper became cheap in modern times",
            "how writing systems developed in ancient times",
            "the history of printing technology in Europe",
            "materials people wrote on before paper was common",
            "the role of professional writers in ancient societies"], 1)],
    [("W", "Hello, class. Last week, we learned how the first writing systems appeared. Today, let's look at "
           "what people wrote on before paper became common. In ancient Mesopotamia, people pressed marks into "
           "soft clay tablets and then dried them in the sun. In China, before paper was invented, people wrote "
           "on thin strips of bamboo tied together with string. In ancient Egypt, people made sheets from the "
           "papyrus plant, which grew along the Nile River. And in medieval Europe, many important books were "
           "written on parchment, which was made from animal skin. Each material shaped how people stored and "
           "shared knowledge. Now, let's look at some pictures of these materials.")])

q(17, 2, 2, [
    ('q', "언급된 재료가 <u>아닌</u> 것은?"),
    ('ch', ["clay", "silk", "bamboo", "papyrus", "animal skin"], 3)])

# =============================================================== 독해 18–45
q(18, 2, 5, [
    ('q', "다음 글의 목적으로 가장 적절한 것은?"),
    ('letter', ["Dear Park Management Team,",
                "My name is Jessica Lee, and I live near Maple Hill Park. I walk along the park’s riverside path "
                "almost every evening, and it has always been one of my favorite places in the neighborhood. "
                "Recently, however, I have noticed that several streetlights along the path are not working. "
                "After sunset, a long section near the bridge becomes completely dark, which makes it difficult "
                "and even dangerous to walk there. Many elderly residents and children use this path, and I am "
                "worried that someone could trip and get hurt. I would greatly appreciate it if you could repair "
                "the broken lights as soon as possible.",
                "Sincerely,", "Jessica Lee"]),
    ('ch', ["공원 산책로 개방 시간 연장을 요청하려고",
            "공원 내 반려동물 출입 제한을 건의하려고",
            "지역 주민 걷기 대회 참가를 신청하려고",
            "공원 청소 자원봉사 활동을 제안하려고",
            "산책로의 고장 난 가로등 수리를 요청하려고"], 1, "tight")])

q(19, 2, 3, [
    ('q', "다음 글에 드러난 Mina의 심경 변화로 가장 적절한 것은?"),
    ('p', "Mina sat backstage, listening to the performer before her. Her hands were cold, and she kept rubbing "
          "them together. What if she forgot the second part of the piece, the one she always got wrong in "
          "practice? When her name was called, she walked to the piano with her heart pounding. She took a deep "
          "breath and began. Her fingers moved smoothly, and the difficult passage flowed out without a single "
          "mistake. As the last note faded, the hall burst into applause. Mina stood up, bowed, and saw her "
          "teacher nodding at her. She lifted her chin and smiled."),
    ('emo', [("bored", "excited"), ("calm", "upset"), ("nervous", "proud"),
             ("hopeful", "disappointed"), ("curious", "indifferent")])])

q(20, 2, 1, [
    ('q', "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?"),
    ('p', "Many meetings fail before they even begin. Participants arrive without knowing why they were invited, "
          "what will be discussed, or what decision is expected at the end. As a result, the first half of the "
          "meeting is spent figuring out its purpose, and the second half is too rushed for careful thinking. "
          "This waste can be avoided with a simple habit. Before calling a meeting, the organizer should state "
          "its goal in one or two sentences and send the agenda to everyone in advance. When participants know "
          "the purpose ahead of time, they can gather information and prepare questions. The meeting itself "
          "then becomes a place for real discussion rather than an introduction to the topic."),
    ('fn', "* agenda: 안건"),
    ('ch', ["회의 전에 목적과 안건을 참석자와 미리 공유해야 한다.",
            "회의 시간은 30분 이내로 제한해야 한다.",
            "모든 참석자가 회의에서 발언할 기회를 가져야 한다.",
            "회의 결과는 문서로 기록하여 보관해야 한다.",
            "중요한 결정은 대면 회의를 통해 내려야 한다."], 1, "tight")])

q(21, 2, 4, [
    ('q', "밑줄 친 <u>a museum of good intentions</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?"),
    ('p', "Walk into almost any home and you will find them: the exercise bike used as a clothes rack, the "
          "language course still in its plastic wrapping, the stack of books bought with great enthusiasm and "
          "never opened. Each of these objects was purchased at a moment of hope. We imagined ourselves cycling every morning, chatting in a new language, or discussing great novels with friends. Buying them felt like taking "
          "the first step toward becoming fitter, smarter, or more skilled. In fact, research suggests that the "
          "act of purchasing can give us a small sense of accomplishment, as if the goal were already partly "
          "achieved. Unfortunately, that feeling can reduce our motivation to do the actual work. We have already enjoyed the pleasure of the plan, so the effort itself begins to feel optional. Over time, our "
          "shelves and closets quietly turn into <u>a museum of good intentions</u>. The solution is not to stop "
          "buying things, but to recognize that owning the tools for change is not the same as changing. Real "
          "progress begins only when the plastic wrapping comes off."),
    ('fn', "* enthusiasm: 열정"),
    ('ch', ["a place that preserves valuable family memories",
            "a collection of items that reflect changing tastes",
            "evidence of careful planning for future goals",
            "a display of plans that were never carried out",
            "a reminder of how much money was spent on luxury"], 1)])

q(22, 2, 2, [
    ('q', "다음 글의 요지로 가장 적절한 것은?"),
    ('p', "There is an old saying that the best way to learn something is to teach it. Modern research supports "
          "this idea. In several studies, students who were told that they would later have to teach the "
          "material to others learned it more effectively than students who were told only to prepare for a "
          "test, even when neither group actually ended up teaching. Simply expecting to explain the material "
          "seemed to change how they studied. They organized information more carefully, looked for the main "
          "ideas, and paid closer attention to how different points were connected. Actually explaining the "
          "material to someone else brings even greater benefits. When we try to put an idea into our own "
          "words, we quickly discover gaps in our understanding that we had not noticed while reading. A "
          "listener’s questions push us to clarify vague points and to find better examples. Even explaining an idea to an imaginary listener can produce some of these benefits. In this way, the "
          "act of explaining turns passive knowledge into something active and well structured. Teachers, it "
          "seems, are often the biggest learners in the classroom."),
    ('fn', "* vague: 모호한"),
    ('ch', ["반복 학습은 장기 기억 형성에 효과적이다.",
            "다른 사람에게 설명하는 과정은 자신의 이해를 깊게 한다.",
            "교사의 피드백은 학생의 학습 동기를 높인다.",
            "협동 학습은 학생의 사회성 발달에 도움을 준다.",
            "학습 내용을 시각화하면 기억하기 쉬워진다."], 1)])

q(23, 2, 5, [
    ('q', "다음 글의 주제로 가장 적절한 것은?"),
    ('p', "Street trees do far more than make a city look attractive. They provide shade, cool the air on hot "
          "days, and absorb rainwater. For these reasons, many cities planted thousands of trees during the "
          "twentieth century. However, to save money and simplify maintenance, planners often chose just a few "
          "species that grew quickly and tolerated urban conditions. This decision later proved costly. When a "
          "disease or insect pest arrived that attacked one of those species, it could spread rapidly from tree "
          "to tree along entire streets. In some cities, a single beetle species killed a large share of the "
          "street trees within a few years, leaving neighborhoods suddenly bare. Experts now recommend that no "
          "single species should make up more than a small percentage of a city’s trees. Diversity, they "
          "argue, is the best protection against the next unexpected threat."),
    ('fn', "* beetle: 딱정벌레"),
    ('ch', ["benefits of planting trees in rural communities",
            "ways to reduce the cost of maintaining city parks",
            "role of street trees in lowering air pollution",
            "methods of protecting trees from extreme weather",
            "risk of relying on a few tree species in cities"], 1)])

q(24, 3, 1, [
    ('q', "다음 글의 제목으로 가장 적절한 것은? [3점]"),
    ('p', "In many English-speaking cultures, silence in a conversation often feels uncomfortable. When a pause "
          "lasts more than a few seconds, people rush to fill it, worried that the silence signals boredom, "
          "disagreement, or awkwardness. In other cultures, however, silence carries very different meanings. "
          "In Japan and Finland, for example, a pause before answering is commonly seen as a sign of respect, "
          "showing that the listener is giving careful thought to what has been said. Responding too quickly "
          "may even seem careless. In such settings, a quiet moment can even be a sign of comfort between friends. These differences can lead to misunderstandings when people from different "
          "backgrounds talk with each other. A speaker who values pauses may be interrupted again and again, "
          "while a speaker who dislikes silence may appear pushy or impatient. Neither side is behaving rudely; "
          "each is simply following the rules it learned. Becoming aware that silence is not empty, but full of "
          "cultural meaning, can help us listen more patiently and judge others less quickly. The next time a "
          "conversation goes quiet, it may be worth waiting a moment before saying anything."),
    ('fn', "* pushy: 지나치게 밀어붙이는"),
    ('ch', ["Mind the Gap: What Silence Means Across Cultures",
            "Why Talking Fast Makes You More Persuasive",
            "The Universal Rules of Polite Conversation",
            "Learning a Language Through Daily Conversation",
            "How Technology Is Changing the Way We Talk"], 1)])

q(25, 2, 3, [
    ('q', "다음 도표의 내용과 일치하지 <u>않는</u> 것은?"),
    ('fig', "fig_r25", 292.8, 198.6),
    ('p', "The graph above shows the results of surveys on how students commuted to school in 2015 and 2025. "
          "The surveys were conducted among students at the same group of middle schools in both years, and each student chose only one way of commuting. ① In both 2015 and 2025, walking was the most common "
          "way students commuted to school, although its percentage decreased by 6 percentage points over the ten years. ② The "
          "percentage of students who commuted by bus decreased by 2 percentage points from 2015 to 2025, while the percentage of students who commuted by car "
          "increased by 4 percentage points. ③ The "
          "percentage of students who commuted by bicycle in 2025 was more than twice that in 2015. ④ In 2025, "
          "the percentage of students who commuted by car was lower than that of students who commuted by bus, "
          "but it was higher than in 2015, when only 18 percent of students came to school by car. ⑤ In 2015, bicycle was the least common way of "
          "commuting, while in 2025, subway was the least common way, chosen by only 11 percent of students.")])

q(26, 2, 4, [
    ('q', "Wangari Maathai에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?"),
    ('p', "Wangari Maathai was born in 1940 in a small village in Kenya. At a time when few girls in her country "
          "attended school, she earned a scholarship to study biology in the United States. After returning "
          "home, she became the first woman in East and Central Africa to earn a doctoral degree. Concerned "
          "about the loss of forests and the hardships it caused rural women, she founded the Green Belt "
          "Movement in 1977. The movement encouraged women to plant trees in their communities, and over the "
          "following decades, it planted tens of millions of trees across Kenya. Maathai also fought for "
          "democracy and human rights, which sometimes led to her arrest. In 2002, she was elected to Kenya’s "
          "parliament. Two years later, she received the Nobel Peace Prize, becoming the first African woman "
          "to win the award."),
    ('fn', "* scholarship: 장학금   ** parliament: 의회"),
    ('ch', ["케냐에서 태어났다.",
            "미국에서 생물학을 공부했다.",
            "1977년에 Green Belt Movement를 설립했다.",
            "2004년에 노벨 문학상을 받았다.",
            "2002년에 국회의원으로 선출되었다."], 1, "tight")])

q(27, 2, 2, [
    ('q', "Summer Coding Camp for Teens에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?"),
    ('notice', "Summer Coding Camp for Teens", [
        ('t', "Learn to create your own apps and games this summer at Lakeside Public Library!"),
        ('kv', "Dates", "July 20 to 24, 2027"),
        ('kv', "Time", "9 a.m. to 12 p.m."),
        ('kv', "Participants", "Students aged 13 to 17"),
        ('kv', "Location", "Room 204, Lakeside Public Library"),
        ('h', "Program Details"),
        ('b', "Days 1 to 3: Learn basic coding skills"),
        ('b', "Day 4: Design your own app with a team"),
        ('b', "Day 5: Present your app to parents and friends"),
        ('b', "No previous coding experience is required."),
        ('b', "Snacks and drinks will be provided during breaks."),
        ('h', "Fee & Registration"),
        ('b', "$150 (lunch included)"),
        ('b', "Each participant must bring his or her own laptop."),
        ('b', "Register on our website by July 10."),
        ('r', "※ For more information, visit www.lakeside*library.org.")]),
    ('ch', ["13세부터 17세까지의 학생이 참가할 수 있다.",
            "수업은 매일 오후에 진행된다.",
            "참가자는 각자 노트북을 가져와야 한다.",
            "참가비에 점심 식사가 포함된다.",
            "마지막 날에 앱 발표회가 열린다."], 1)])

q(28, 2, 5, [
    ('q', "Night Tour at Riverside Zoo에 관한 다음 안내문의 내용과 일치하는 것은?"),
    ('notice', "Night Tour at Riverside Zoo", [
        ('t', "See what our animals do after dark on a guided night tour with our experienced zookeepers! It is a "
              "special chance to watch owls, bats, and other night animals up close."),
        ('kv', "When", "Every Friday and Saturday, 8:00 p.m. to 9:30 p.m."),
        ('kv', "Meeting Point", "Main Gate"),
        ('h', "Tickets"),
        ('tbl', ["Visitor", "Price", "Notes"],
         [["Adult", "$25", "ages 13 and over"],
          ["Child", "$10", "ages 6 to 12"]]),
        ('h', "Notes"),
        ('b', "Children under 6 are not allowed on the tour."),
        ('b', "Tickets are available only on our website."),
        ('b', "Flashlights are not allowed, as bright light can disturb the animals."),
        ('b', "Each tour group is limited to 20 people."),
        ('b', "Visitors must stay with the guide at all times."),
        ('b', "Comfortable shoes are recommended."),
        ('r', "※ Tours may be canceled in case of heavy rain."),
        ('r', "※ For more information, visit www.riverside*zoo.org.")]),
    ('ch', ["매일 밤 운영된다.",
            "어린이는 무료로 참가할 수 있다.",
            "투어는 세 시간 동안 진행된다.",
            "손전등을 대여해 준다.",
            "온라인으로만 표를 구매할 수 있다."], 1)])

q(29, 2, 1, [
    ('q', "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?"),
    ('p', "Octopuses are among the most intelligent invertebrates, and their abilities continue ① <u>to "
          "surprising</u> researchers. In laboratory studies, octopuses have learned to open jars, ② <u>escape</u> "
          "from tanks, and even recognize individual people. Some have been observed carrying coconut shells to "
          "use as portable shelters. Octopuses are also masters of disguise, changing both the color and the texture of their skin within a fraction of a second. What makes these achievements remarkable is that octopuses live short, "
          "solitary lives, so they have little opportunity to learn from others. Unlike humans, ③ <u>whose</u> "
          "knowledge is passed down through generations, each octopus must figure out the world largely on its "
          "own. Scientists believe that the octopus brain, with most of its neurons ④ <u>located</u> in the arms "
          "rather than the head, allows each arm to explore and respond to its surroundings with surprising "
          "independence. Studying such a different kind of mind ⑤ <u>helps</u> researchers rethink what "
          "intelligence is and how it can develop."),
    ('fn', "* invertebrate: 무척추동물   ** solitary: 혼자 사는")])

q(30, 3, 3, [
    ('q', "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]"),
    ('p', "In the early days of aviation, pilots relied on their own senses to judge whether a plane was level. "
          "However, this method proved ① <u>dangerous</u> in clouds or darkness, where the body’s sense of "
          "balance can be easily fooled. A pilot flying in thick fog might feel perfectly level while the plane "
          "is actually turning, a condition that has led to many accidents. To solve this problem, engineers "
          "developed instruments that ② <u>measure</u> the plane’s position independently of human perception. "
          "At first, many experienced pilots were ③ <u>eager</u> to trust these devices, insisting that their "
          "own feelings were more reliable. Training programs therefore had to teach pilots to ④ <u>ignore</u> "
          "what their bodies were telling them and believe the instruments instead. This was not easy, because "
          "the sensations were extremely convincing. Over time, however, flying by instruments became standard "
          "practice, and it made air travel far ⑤ <u>safer</u> than before. The lesson extends beyond aviation: "
          "sometimes our most confident impressions are exactly the ones that need to be checked against "
          "objective evidence."),
    ('fn', "* aviation: 비행")])

q(31, 2, 4, [
    ('p0', "For a long time, doctors focused almost entirely on choosing the right drug and the right dose. More "
           "recently, however, researchers have begun to pay attention to another factor: <blank:24>. The human "
           "body follows daily rhythms that affect blood pressure, body temperature, hormone levels, and the activity of many "
           "organs. Because of these rhythms, the same medicine can behave quite differently depending on the "
           "hour. For example, some blood pressure drugs appear to work better when taken in the evening, when "
           "the body is preparing for sleep, than when taken in the morning. Certain cancer treatments also seem "
           "to cause fewer side effects if they are given at particular times of day, when healthy cells are "
           "less active. Even the effectiveness of vaccines may vary depending on whether they are given in the morning or in the afternoon. These findings suggest that asking when a patient should take a medicine may be as "
           "important as asking which medicine to take. As a result, a new field called chronotherapy has "
           "emerged, aiming to match treatments to the body’s internal clock."),
    ('fn', "* chronotherapy: 시간 요법"),
    ('ch', ["speed", "beauty", "cost", "timing", "quantity"], 2)])

q(32, 3, 2, [
    ('p0', "It is tempting to believe that creativity flourishes best when there are no limits. Give people "
           "unlimited time, money, and freedom, the thinking goes, and they will produce their best ideas. In "
           "practice, however, the opposite is often true. When the famous children’s author Dr. Seuss was "
           "challenged to write a book using only fifty different words, he produced <i>Green Eggs and Ham</i>, "
           "one of the best-selling children’s books of all time. Poets have long known this as well; the strict rules of the sonnet have inspired some of the most inventive poems in the English language. Studies support this pattern. In one "
           "experiment, participants who were asked to design a toy using a limited set of parts came up with "
           "more original designs than those who could use any parts they wanted. Limits seem to force people "
           "away from the obvious solutions that come to mind first, pushing them to search more widely and "
           "combine ideas in unexpected ways. For those who wish to think creatively, then, the best strategy "
           "may be to <blank:44>. [3점]"),
    ('ch', ["wait until enough resources become available",
            "deliberately place restrictions on their own work",
            "collect as many different opinions as possible",
            "avoid comparing their ideas with those of others",
            "focus on improving ideas that already exist"], 1)])

q(33, 2, 5, [
    ('p0', "Experts are often surprisingly poor teachers of beginners. This is not because they lack knowledge, "
           "but in a sense because they have too much of it. Once we have learned something well, it becomes "
           "difficult to imagine what it was like not to know it, or to remember the confusion we once felt. In a well-known study, participants were asked "
           "to tap out the rhythm of a familiar song, such as ‘Happy Birthday,’ while listeners tried to guess "
           "the song. The tappers predicted that listeners would guess correctly about half the time, but in "
           "fact listeners succeeded only once in forty attempts. The tappers could hear the melody in their "
           "heads, so the tapping seemed obvious to them; the listeners heard only a series of knocks. Even when they were told how difficult the task was, many tappers still could not believe that listeners had failed to recognize such a familiar song. Experts "
           "face the same problem when they skip steps that seem too simple to mention or use terms they have "
           "long taken for granted. To communicate effectively, therefore, experts must make a deliberate effort "
           "to <blank:40>."),
    ('ch', ["acquire more advanced knowledge in their field",
            "speak with confidence about what they know",
            "ask learners to study the basics on their own",
            "rely on familiar examples from their own work",
            "see the material from the perspective of a beginner"], 1)])

q(34, 3, 1, [
    ('p0', "Many people spend a great deal of time and money searching for the perfect gift, assuming that a "
           "more expensive present will be more appreciated. Research on gift-giving, however, tells a different "
           "story. In several studies, givers believed that pricier gifts would be valued more highly, yet "
           "recipients reported no greater appreciation for expensive gifts than for cheaper ones. What "
           "recipients did value was evidence that the giver had listened to them. A secondhand book by a "
           "favorite author, a recipe card for a dish mentioned months earlier, or a simple tool that solved a "
           "small daily problem often meant more than an impressive but impersonal gift. Another study found that recipients were often happier with practical gifts they could use every day than with luxurious items that would be used only once. Givers, by contrast, tend to focus on the moment the gift is opened, while recipients think about how they will live with it afterward. A handwritten note explaining the choice can add value too. In the end, a gift seems to be "
           "appreciated less for its price or novelty than for <blank:44>. [3점]"),
    ('fn', "* impersonal: 개인적이지 않은"),
    ('ch', ["the sign that the giver has paid attention to the receiver",
            "the effort the giver made to wrap it beautifully",
            "the surprise it creates at the moment of opening",
            "the social status that it brings to the receiver",
            "the long time the giver spent searching for it"], 1)])

q(35, 2, 3, [
    ('q', "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?"),
    ('p', "Most students know that sleep is important for health, but fewer realize how closely it is tied to "
          "memory. Scientists have studied this connection for more than a century, and recent brain-imaging research has made it clearer than ever. During the day, the brain takes in a large amount of new information, much of which is "
          "stored only temporarily. ① While we sleep, the brain replays the day’s experiences, strengthening the "
          "connections that represent important memories. ② This process helps explain why students who sleep "
          "well after studying often perform better on tests than those who stay up all night. ③ Many students "
          "also drink coffee in the evening, and the price of coffee has risen sharply over the past decade. "
          "④ Sleep also appears to help the brain organize information, linking new knowledge to what is "
          "already known and sometimes revealing patterns that were missed while awake. ⑤ For these reasons, "
          "giving up sleep to gain more study time may actually undermine the very learning it is meant to "
          "support.")])

q(36, 2, 4, [
    ('box', [('p', "Bees are famous for making honey, but their most valuable contribution to humans may be "
                   "pollination. Many of the fruits and vegetables we eat depend on bees to carry pollen from one "
                   "flower to another.")]),
    ('pl', "(A)", "This decline has worried farmers, some of whom now rent hives and transport them from farm to "
                  "farm during the flowering season. Without these traveling bees, harvests of crops such as "
                  "almonds and blueberries would fall dramatically."),
    ('pl', "(B)", "Renting bees, however, is only a temporary solution. To protect pollinators in the long term, "
                  "experts recommend planting a wider variety of flowers along fields and roadsides, giving wild "
                  "bees the food and shelter they need to survive."),
    ('pl', "(C)", "In recent decades, however, bee populations in many regions have declined sharply. Scientists "
                  "point to several causes, including the loss of wild flowers, the use of certain pesticides, and "
                  "the spread of diseases among hives."),
    ('fn', "* pollination: 수분(受粉)   ** pesticide: 살충제"),
    ('ord', ORD3)])

q(37, 3, 1, [
    ('box', [('p', "In the nineteenth century, most towns set their clocks by the position of the sun, so noon "
                   "in one city could differ by several minutes from noon in a city just a few miles away. Each town considered its own local time to be perfectly natural and "
                   "correct.")]),
    ('pl', "(A)", "For most of history, this caused few problems, since people rarely traveled fast enough to "
                  "notice the difference. A traveler on horseback could simply adjust his watch at the end of a long journey. The arrival of the railway, however, changed everything."),
    ('pl', "(B)", "To solve this problem, railway companies began to adopt standard time zones, in which all "
                  "clocks across a wide area showed the same hour. Over time, governments followed, and the time "
                  "zones we use today became part of everyday life around the world. [3점]"),
    ('pl', "(C)", "The faster trains made these local differences impossible to ignore. Railway companies "
                  "struggled to publish timetables when every station kept its own time, and the confusion "
                  "sometimes led to dangerous accidents on shared tracks. Passengers, too, often missed their trains because their "
                  "watches did not match the station clocks."),
    ('fn', "* timetable: 시간표"),
    ('ord', ORD3)])

q(38, 2, 2, [
    ('box', [('p', "He argued that clear rules can make drivers feel so safe that they stop paying attention to "
                   "what is happening around them.")]),
    ('p', "For decades, traffic engineers assumed that more signs, signals, and barriers would make roads safer. "
          "( ① ) In the early 2000s, however, a Dutch engineer named Hans Monderman challenged this assumption. "
          "( ② ) To test his idea, he removed traffic lights, road markings, and even curbs from several busy "
          "intersections, leaving drivers, cyclists, and pedestrians to share the same open space. ( ③ ) Without "
          "clear instructions, drivers slowed down and began to make eye contact with others before moving "
          "through the intersection. ( ④ ) Surprisingly, the number of accidents did not rise; in several "
          "places, it actually fell. Pedestrians and cyclists, too, reported feeling more comfortable crossing the space. ( ⑤ ) The experiment suggests that safety sometimes depends less on rules "
          "than on the attention and caution that people bring to a situation. Similar designs have since been tried in cities across Europe, with "
          "mixed but often encouraging results."),
    ('fn', "* curb: (인도의) 연석   ** intersection: 교차로")])

q(39, 3, 5, [
    ('box', [('p', "This is why the same joke can be hilarious in one room and fall completely flat in "
                   "another.")]),
    ('p', "We usually think of laughter as a response to something funny, such as a clever joke or a silly scene in a movie. ( ① ) Yet researchers who have "
          "observed people in everyday settings have found that most laughter follows remarks that are not "
          "jokes at all, such as ‘See you later’ or ‘I know.’ ( ② ) Laughter, it seems, is less about humor than "
          "about relationships. ( ③ ) It signals friendliness, eases tension, and shows that we share a point of "
          "view with the people around us. Even babies laugh most when they are playing with others. ( ④ ) This social function becomes clear when we compare laughing "
          "alone with laughing in company: people are far more likely to laugh with others, even while watching "
          "the same comedy. ( ⑤ ) In other words, whether a joke works depends heavily on who is in the room "
          "and how they feel about one another. [3점]"),
    ('fn', "* hilarious: 아주 우스운")])

q(40, 2, 4, [
    ('q', "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?"),
    ('box', [('p', "In a well-known experiment, college students were asked to put on a T-shirt printed with a "
                   "large picture of a singer whom most students considered embarrassing. Each student then "
                   "walked into a room where other students were already sitting and filling out "
                   "questionnaires. Afterward, the students wearing the shirt were asked to estimate how many "
                   "people in the room had noticed it. On average, they guessed that about half of the observers "
                   "had noticed the shirt. In reality, only about a quarter had. When the "
                   "researchers repeated the study with a more flattering shirt, the wearers again overestimated how many people had noticed. The researchers called this the "
                   "‘spotlight effect.’ Because we experience the world from inside our own heads, our own "
                   "appearance and actions seem highly visible to us, and we assume others are paying just as "
                   "much attention. Most people, however, are busy thinking about themselves and have little attention left for others. The same bias may "
                   "explain why we worry for days about a small mistake in a presentation that our audience has "
                   "already forgotten."),
             ('fn', "* questionnaire: 설문지")]),
    ('arrow',),
    ('summary', "People tend to <ublank:(A)> how much others notice their appearance and mistakes, mainly "
                "because they are <ublank:(B)> in their own point of view."),
    ('ab', [("ignore", "absorbed"), ("ignore", "lost"), ("exaggerate", "confident"),
            ("exaggerate", "absorbed"), ("accept", "lost")])])

# 41–42 장문
P41 = [
    "Most of us try hard to appear flawless, especially in front of people we want to impress. We hide our "
    "mistakes and present only our best side, assuming that any sign of imperfection will (a) <u>increase</u> "
    "others’ respect for us. Research suggests that this assumption is not always correct. In a classic "
    "experiment, participants listened to a recording of a candidate for a quiz team who answered nearly every "
    "question correctly. In one version of the recording, the candidate clumsily spilled a cup of coffee at the "
    "end. Surprisingly, listeners rated the highly competent candidate as (b) <u>more</u> likable when he made "
    "this small mistake.",
    "Psychologists call this the ‘pratfall effect.’ A minor error seems to make an impressive person appear "
    "more human and approachable, reducing the (c) <u>distance</u> that others feel between themselves and "
    "someone who seems perfect. However, the effect has limits. When the candidate who spilled the coffee had "
    "performed poorly on the quiz, the same accident made listeners like him even less. A mistake, in other "
    "words, helps only those who have already shown their (d) <u>competence</u>.",
    "These findings carry a useful lesson for leaders, teachers, and anyone in a position of authority. "
    "Admitting an occasional error or laughing at a small slip can build trust and make others feel more "
    "comfortable approaching you. Constantly hiding every flaw, on the other hand, may make you seem "
    "(e) <u>distant</u> and difficult to relate to. Perfection, it turns out, is not always the most "
    "attractive quality.",
]
P41_FN = "* pratfall: 실수, 엉덩방아"
q(41, 3, 3, [
    ('q', "윗글의 제목으로 가장 적절한 것은? [3점]"),
    ('ch', ["How to Avoid Embarrassing Mistakes in Public",
            "Why Competence Matters More Than Likability",
            "The Charm of Imperfection: Mistakes Can Help",
            "Coffee and Concentration: A Surprising Link",
            "Hiding Your Flaws: The Secret of Great Leaders"], 1)])
q(42, 2, 1, [
    ('q', "밑줄 친 (a)～(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?"),
    ('ch', ABCDE, 5)])

# 43–45 장문
P43 = {
    "(A)": "Hana had always wanted to ride to school like her friends, but her family could not afford a new "
           "bicycle. One afternoon, while walking past Mr. Collins’s garage, she noticed an old, rusty bicycle "
           "leaning against the wall. Mr. Collins, a retired mechanic, saw her looking at it. “It hasn’t moved in "
           "ten years,” (a) <u>he</u> said with a smile. “If you’re willing to work on it, it’s yours.” Hana’s eyes "
           "widened. “Really? I’ll come every day after school!”",
    "(B)": "Next came the harder part. The chain was broken, and the brakes no longer worked. Mr. Collins could "
           "have fixed everything himself in an hour, but (b) <u>he</u> chose to guide Hana step by step instead. He showed her how to measure the brake cable, cut it to the right length, and tighten each bolt just enough. "
           "“If you build it, you’ll know how to fix it,” he told her. Hana made plenty of mistakes, and her hands were covered in grease, but each "
           "time she tried again. When the new chain finally clicked into place, she let out a cheer, and the old man "
           "laughed with her.",
    "(C)": "The next day, Hana arrived at the garage right after class. Mr. Collins handed her a pair of gloves "
           "and a brush. “First, we clean,” he said. For a whole week, Hana scrubbed away rust and dirt while "
           "(c) <u>he</u> explained how each part worked. Some days her arms ached, but she never once complained. "
           "Slowly, the bicycle began to look less like a piece of junk and more like something that "
           "could actually carry her to school. Mr. Collins nodded with approval at her work.",
    "(D)": "At the end of the second week, the bicycle was ready. It had a fresh coat of blue paint that Hana had "
           "chosen herself. She rode it slowly around the block while Mr. Collins watched from the garage door "
           "with (d) <u>his</u> arms folded and a proud smile on his face. The next morning, Hana rode to school "
           "for the first time. Her friends gathered around the bike rack, asking where she had found such a beautiful bicycle. When she came home, she handed Mr. Collins a card that (e) <u>she</u> had made "
           "during lunch. It read, “Thank you for teaching me more than how to fix a bike.”",
}
q(43, 2, 2, [
    ('q', "주어진 글 (A)에 이어질 내용을 순서에 맞게 배열한 것으로 가장 적절한 것은?"),
    ('ord', ORD4)])
q(44, 2, 5, [
    ('q', "밑줄 친 (a)～(e) 중에서 가리키는 대상이 나머지 넷과 <u>다른</u> 것은?"),
    ('ch', ABCDE, 5)])
q(45, 2, 3, [
    ('q', "윗글에 관한 내용으로 적절하지 <u>않은</u> 것은?"),
    ('ch', ["Hana의 가족은 새 자전거를 살 형편이 되지 않았다.",
            "Mr. Collins는 은퇴한 정비사였다.",
            "Hana는 녹을 닦는 일이 힘들다고 자주 불평했다.",
            "자전거의 체인이 끊어져 있었다.",
            "Hana는 자전거를 칠할 파란색을 직접 골랐다."], 1)])

# =============================================================== 회차별 자체 점검 (verify.py 가 호출)
ORDER_KEY = {36: "(C) － (A) － (B)", 37: "(A) － (C) － (B)", 43: "(C) － (B) － (D)"}
FIG_TEXT = {
    "fig_l04": "[그림] 과학 축제 부스: ① 'SCIENCE FAIR' 현수막 ② 체크무늬 식탁보 ③ 탁자 위 화산 모형 "
               "④ 탁자 아래 화분 두 개 ⑤ 벽의 태양계 포스터",
    "fig_r25": "[도표] How Students Commuted to School (2015 / 2025): Walking 34/28, Bus 26/24, Car 18/22, "
               "Bicycle 8/15, Subway 14/11 (%)",
}


def self_checks():
    """계산으로 정답이 정해지는 문항(6·10·25번)을 다시 계산한다. [(설명, 참/거짓)]"""
    out = []
    total = (10 * 3 + 20) * 0.9
    ch6 = [b for b in Q[6]["blocks"] if b[0] == "ch"][0][1]
    out.append((f"6번: (장미 10 × $3 + 꽃병 $20) × 0.9 = ${total:.0f}", ch6[Q[6]["ans"] - 1] == f"${total:.0f}"))
    rows = [b for b in Q[10]["blocks"] if b[0] == "tbl10"][0][3]
    ok = [r[0] for r in rows if int(r[1][1:]) <= 45 and int(r[2]) >= 5 and r[4] == "○" and r[3] == "White"]
    out.append((f"10번: 조건을 만족하는 모델 {ok}", ok == ["ABCDE"[Q[10]["ans"] - 1]]))
    a, b = dict(W=34, B=26, C=18, Bi=8, S=14), dict(W=28, B=24, C=22, Bi=15, S=11)
    truth = [max(a, key=a.get) == "W" == max(b, key=b.get) and b["W"] < a["W"],
             a["B"] - b["B"] == 2,
             b["Bi"] > 2 * a["Bi"],
             b["C"] < b["B"] and b["C"] > a["C"],
             min(a, key=a.get) == "Bi" and min(b, key=b.get) == "S"]
    out.append((f"25번: 거짓 문장 {[i + 1 for i, t in enumerate(truth) if not t]}",
                [i + 1 for i, t in enumerate(truth) if not t] == [Q[25]["ans"]]))
    return out


# =============================================================== 쪽 배치 (원본 홀수형과 동일)
SET = {
    16: "[16～17] 다음을 듣고, 물음에 답하시오.",
    31: "[31～34] 다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.",
    36: "[36～37] 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것을 고르시오.",
    38: "[38～39] 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.",
    41: "[41～42] 다음 글을 읽고, 물음에 답하시오.",
    43: "[43～45] 다음 글을 읽고, 물음에 답하시오.",
}
# 항목: 문항 번호, 'NOTICE'(듣기 안내), 'END'(듣기 끝 안내), ('set', 첫 번호), ('long', 41) 장문 지문,
#       ('part', '(A)') 43–45 장문 단락
LAYOUT = [
    (['NOTICE', 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]),
    ([13, 14, 15, ('set', 16), 16, 17, 'END'], [18, 19, 20]),
    ([21, 22], [23, 24]),
    ([25, 26], [27, 28]),
    ([29, 30], [('set', 31), 31, 32]),
    ([33, 34], [35, ('set', 36), 36]),
    ([37, ('set', 38), 38], [39, 40]),
    ([('set', 41), ('long', 41), 41, 42, ('set', 43), ('part', '(A)')],
     [('part', '(B)'), ('part', '(C)'), ('part', '(D)'), 43, 44, 45]),
]
