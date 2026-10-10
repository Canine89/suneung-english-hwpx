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
q(1, 2, 4, [
    ('q', "다음을 듣고, 남자가 하는 말의 목적으로 가장 적절한 것을 고르시오."),
    ('ch', ["도서관 열람실 운영 시간 연장을 안내하려고",
            "도서 반납 기한을 지켜 줄 것을 당부하려고",
            "독서 동아리 신규 회원 모집을 홍보하려고",
            "도서관 좌석 예약 앱의 사용법을 설명하려고",
            "도서관 리모델링 공사 일정을 공지하려고"], 1)],
    [("M", "Hello, students. This is Mr. Harris, your school librarian. As many of you know, it has been hard "
           "to find an empty seat in the library during exam weeks. So starting next Monday, you'll reserve "
           "library seats with our new app, LibSeat. Let me explain how it works. First, download LibSeat and "
           "log in with your student ID number. Next, open the seat map and choose any seat shown in green. "
           "Then, tap the Reserve button. When you arrive, you must scan the QR code on your desk within fifteen "
           "minutes, or your reservation will be canceled automatically. If you leave for more than thirty "
           "minutes, please tap the Away button so that others know the seat is still in use. I hope this app "
           "makes studying in the library more comfortable. Thank you.")])

q(2, 2, 2, [
    ('q', "대화를 듣고, 여자의 의견으로 가장 적절한 것을 고르시오."),
    ('ch', ["수업 전에 교과서를 미리 읽어 두어야 한다.",
            "손으로 필기하면 수업 내용을 더 오래 기억할 수 있다.",
            "노트북으로 필기하면 정보를 빠르게 정리할 수 있다.",
            "필기한 내용은 친구들과 공유하는 것이 바람직하다.",
            "수업 중에는 전자 기기 사용을 자제해야 한다."], 1)],
    [("M", "Jenny, I'm thinking of buying a tablet to take notes in class."),
     ("W", "Really? Why do you want one, Tom?"),
     ("M", "I can type much faster than I can write. I'd be able to record almost everything the teacher says."),
     ("W", "That's true, but writing everything down isn't always the best way to learn."),
     ("M", "What do you mean?"),
     ("W", "When I take notes by hand, I can't write every word, so I have to think about what's important "
           "and put it in my own words."),
     ("M", "Hmm, I never thought about it that way."),
     ("W", "That process helps me understand the lesson, and I remember it much longer, even weeks later."),
     ("M", "So you're saying handwriting helps memory?"),
     ("W", "Exactly. I'd say taking notes by hand keeps the lesson in your head longer than typing does."),
     ("M", "Okay. Maybe I'll try using a notebook for a week before I buy a tablet.")])

q(3, 2, 5, [
    ('q', "다음을 듣고, 남자가 하는 말의 요지로 가장 적절한 것을 고르시오.", {"sp": -15}),
    ('ch', ["작은 습관의 변화가 건강한 삶의 출발점이 된다.",
            "충분한 수면은 학습 능률을 높이는 데 필수적이다.",
            "목표를 구체적으로 세우면 동기 부여에 도움이 된다.",
            "실수를 기록하는 습관은 문제 해결 능력을 길러 준다.",
            "잠들기 전 감사한 일을 적으면 마음이 안정된다."], 1)],
    [("M", "Hello, listeners. Welcome back to Mind Matters. Do you often go to bed with your head full of "
           "worries? Many people replay the stressful moments of the day again and again before they fall "
           "asleep. Here's a simple tip. Before you go to bed, take out a notebook and write down three things "
           "you were thankful for that day. They don't have to be big. Maybe a friend shared lunch with you, "
           "or the bus came right on time. When you focus on these moments, your mind moves away from your "
           "worries, and you begin to feel calm. Writing them down at the end of the day helps you settle "
           "your feelings and end the day peacefully. Why not try it tonight?")])

q(4, 2, 4, [
    ('q', "대화를 듣고, 그림에서 대화의 내용과 일치하지 <u>않는</u> 것을 고르시오.", {"sp": -10}),
    ('fig', "fig_l04", 306.2, 187.2)],
    [("W", "Dad, look at this picture. It's the campsite I set up with my club members last weekend."),
     ("M", "Wow, Sophia. Let me see. There's a banner that says CAMP between the two trees."),
     ("W", "Yes. We made it ourselves to welcome the new members."),
     ("M", "Nice. I like the dome tent with the star pattern. It looks cozy."),
     ("W", "It was. We slept in it for two nights."),
     ("M", "And there's a round table with a lantern on it."),
     ("W", "Right. We had dinner around that table and talked late into the night."),
     ("M", "I see two bicycles leaning against the tree. Did you ride them there?"),
     ("W", "Yes. We rode along the lake trail on Saturday morning."),
     ("M", "Sounds fun. Oh, and the puppy sleeping on the mat is so cute!"),
     ("W", "That's Max, our club leader's dog. He went everywhere with us.")])

q(5, 2, 3, [
    ('q', "대화를 듣고, 여자가 할 일로 가장 적절한 것을 고르시오."),
    ('ch', ["가격표 만들기", "포스터 붙이기", "테이블 빌리기", "쿠키 굽기", "모금함 꾸미기"], 2)],
    [("M", "Ms. Parker, our class charity bake sale is tomorrow. Everything's almost ready."),
     ("W", "Great job, Eric. Did you make the price tags?"),
     ("M", "Yes. Lucy and I finished them this morning."),
     ("W", "Good. How about the posters?"),
     ("M", "We put them up in the hallway yesterday. And the cookies will be baked tonight at Kevin's house."),
     ("W", "Wonderful. What about the donation box?"),
     ("M", "Mina decorated it with ribbons. It looks really nice. But we still have a problem."),
     ("W", "What is it?"),
     ("M", "We need two more tables to display everything, but the student council has already lent "
           "theirs out."),
     ("W", "Don't worry. The science lab has some folding tables. I'll go and borrow two of them for you."),
     ("M", "Thank you so much, Ms. Parker.")])

q(6, 2, 2, [
    ('q', "대화를 듣고, 남자가 지불할 금액을 고르시오."),
    ('ch', ["$54", "$60", "$66", "$72", "$75"], 5)],
    [("W", "Welcome to Blue Harbor Boat Tours. How may I help you?"),
     ("M", "Hi. I'd like to buy tickets for the two o'clock tour. How much are they?"),
     ("W", "Adult tickets are $30, and tickets for children under twelve are $15."),
     ("M", "Then two adults and one child, please. My son is eight."),
     ("W", "All right. That's two adult tickets and one child ticket."),
     ("M", "Also, I have this coupon from the city tourist center. Can I use it?"),
     ("W", "Let me check. Yes, it gives you 20% off the total price."),
     ("M", "Great. Do I need to pay extra for life jackets?"),
     ("W", "No, they're included. So you get 20% off the total."),
     ("M", "Perfect. Here's my credit card.")])

q(7, 2, 5, [
    ('q', "대화를 듣고, 여자가 과학 축제 자원봉사에 참여할 수 <u>없는</u> 이유를 고르시오."),
    ('ch', ["동생을 돌봐야 해서", "수학 과제를 끝내야 해서", "발목을 다쳐서",
            "가족 여행을 가야 해서", "할머니 생신 파티가 있어서"], 1, 149)],
    [("M", "Hey, Grace. Are you going to volunteer at the city science festival this Saturday?"),
     ("W", "I really wanted to, Brian. But I can't make it."),
     ("M", "That's too bad. Do you have to look after your little brother again?"),
     ("W", "No, my parents will be home this weekend."),
     ("M", "Then is it because of the math assignment? It's due on Monday."),
     ("W", "I already finished it. It wasn't that hard."),
     ("M", "Oh, good. How's your ankle? I heard you hurt it during the soccer game."),
     ("W", "It's fine now. Actually, it's my grandmother's 80th birthday on Saturday, and my whole family "
           "is having a party for her."),
     ("M", "I see. That's important. I hope you have a great time."),
     ("W", "Thanks. Maybe I can join next year.")])

q(8, 2, 3, [
    ('q', "대화를 듣고, Riverside Night Market에 관해 언급되지 <u>않은</u> 것을 고르시오."),
    ('ch', ["장소", "운영 시간", "입장료", "대표 메뉴", "주차 방법"], 3)],
    [("W", "Jake, have you heard about the Riverside Night Market?"),
     ("M", "No, I haven't. What is it?"),
     ("W", "It's a market that opens every Friday night this summer. It's held in Riverside Park, "
           "right next to the bridge."),
     ("M", "Sounds interesting. What time does it open?"),
     ("W", "It runs from 6 p.m. to 11 p.m."),
     ("M", "What can you buy there?"),
     ("W", "All kinds of things, but the most popular item is the grilled corn with cheese. "
           "People wait in line for it."),
     ("M", "I'd love to try it. Is it easy to get there by car?"),
     ("W", "Yes, but the park's parking lot fills up quickly. Visitors are asked to park at the city hall "
           "and take the free shuttle bus."),
     ("M", "Great. Let's go together this Friday.")])

q(9, 2, 1, [
    ('q', "2027 Youth Robotics Camp에 관한 다음 내용을 듣고, 일치하지 <u>않는</u> 것을 고르시오."),
    ('ch', ["7월 14일부터 사흘간 진행된다.",
            "중학생과 고등학생이 참가할 수 있다.",
            "참가자들은 팀을 이루어 로봇을 제작한다.",
            "마지막 날에 시상식이 열린다.",
            "온라인으로 신청해야 한다."], 1, 149)],
    [("W", "Hello, everyone. I'm Diane Moore, director of the Greenville Science Center. I'm happy to "
           "announce the 2027 Youth Robotics Camp. The camp will run for five days, from July 14th to "
           "July 18th. It is open to all middle and high school students in our city. During the camp, "
           "participants will work in teams of four to design and build their own robots. Experienced "
           "engineers from local companies will guide each team. On the last day, the teams will "
           "compete in a robot challenge, and an awards ceremony will follow. The participation fee is "
           "$100, which includes all materials and lunch. To sign up, please visit our website and fill "
           "out the online application form by June 30th. Don't miss this chance!")])

q(10, 2, 3, [
    ('q', "다음 표를 보면서 대화를 듣고, 여자가 구입할 캠핑 랜턴을 고르시오."),
    ('tbl10', "Camping Lanterns",
     ["Model", "Price", "Battery|Life", "Weight", "Water-|proof"],
     [["A", "$25", "10 hours", "300g", "×"],
      ["B", "$32", "12 hours", "450g", "○"],
      ["C", "$38", "15 hours", "400g", "○"],
      ["D", "$45", "20 hours", "350g", "×"],
      ["E", "$52", "24 hours", "500g", "○"]])],
    [("M", "Hi, Amy. What are you looking at?"),
     ("W", "I'm choosing a camping lantern for my trip next month. Can you help me?"),
     ("M", "Sure. Let's see. How much do you want to spend?"),
     ("W", "I don't want to spend more than $50."),
     ("M", "Okay, then this one is out. What about battery life?"),
     ("W", "I'll be camping for three nights, so it should last at least 12 hours."),
     ("M", "Then you can't choose Model A. Do you need a waterproof one?"),
     ("W", "Definitely. It often rains in the mountains."),
     ("M", "Then you have two options left. How about the weight?"),
     ("W", "I'll carry it in my backpack, so it should weigh less than 450 grams."),
     ("M", "Then this one is the only choice."),
     ("W", "Great. I'll order it now.")])

q(11, 2, 1, [
    ('q', "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오."),
    ('ch', ["Sure. I'll be there with an umbrella in ten minutes.",
            "No problem. The bus stop has been moved recently.",
            "Sorry. I've already lent my umbrella to your brother.",
            "Great. You should check the weather before you leave.",
            "Okay. I'll buy you a new umbrella this weekend."], 1, 149)],
    [("M", "Hi, Emma. Where are you now? It's getting dark."),
     ("W", "Dad, I'm at the bus stop near school, but I left my umbrella in the classroom, and it's pouring. "
           "Could you come and pick me up?"),
     ("M", "")])

q(12, 3, 5, [
    ('q', "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]"),
    ('ch', ["I'm afraid the essay contest was canceled.",
            "Don't worry. I'll print the essay for you.",
            "Good job. Your essay won first prize.",
            "Sorry, but you should've chosen another topic.",
            "Of course. Just upload the correct one by tonight."], 1, 149)],
    [("W", "Hi, Jason. You look worried. What's up?"),
     ("M", "Ms. Lee, I submitted my history essay online, but I think I uploaded the wrong file. "
           "Can I send it again?"),
     ("W", "")])

q(13, 3, 2, [
    ('q', "대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]"),
    ('speaker', "Man:"),
    ('ch', ["I'm sorry, but we don't sell chocolate cakes anymore.",
            "No problem. We'll have it ready for you by ten.",
            "You can write the birthday message on the card yourself.",
            "Unfortunately, delivery isn't available on weekends.",
            "Then you'll need to pay the full price in advance."], 1)],
    [("M", "Sweet Oven Bakery. How can I help you?"),
     ("W", "Hi. I ordered a birthday cake online yesterday. My name is Linda Clark."),
     ("M", "Let me check. Yes, a chocolate cake for pickup this Saturday at 11 a.m., right?"),
     ("W", "That's right. But I'd like to change the message on the cake. Is that possible?"),
     ("M", "Sure. What would you like it to say?"),
     ("W", "Please write \"Happy 10th Birthday, Chloe\" instead of just \"Happy Birthday.\""),
     ("M", "Okay. I've changed it. Anything else?"),
     ("W", "Actually, yes. The party starts earlier than I expected."),
     ("M", "I see. Do you want to change the pickup time, then?"),
     ("W", "Yes. Could I possibly pick it up an hour earlier, at 10 a.m.?"),
     ("M", "")])

q(14, 3, 1, [
    ('q', "대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]"),
    ('speaker', "Woman:"),
    ('ch', ["Sounds great. I'd love to come along and try it.",
            "Too bad. The vegetables didn't grow well this year.",
            "Right. You should buy some seeds in advance.",
            "Never mind. I already have a garden at home.",
            "Sorry. I'm not interested in growing flowers."], 1)],
    [("W", "Kevin, you look tanned. Have you been traveling?"),
     ("M", "Not at all, Hannah. I've been working at the community garden near my apartment."),
     ("W", "A community garden? What's that?"),
     ("M", "It's a shared garden where neighbors grow vegetables together. Each person takes care of a "
           "small plot."),
     ("W", "That sounds nice. What do you grow there?"),
     ("M", "Tomatoes, lettuce, and peppers. Last week, I picked my first tomatoes."),
     ("W", "Wow. I've always wanted to grow my own vegetables, but I don't have a yard."),
     ("M", "That's exactly why the garden is great. You don't need any space of your own."),
     ("W", "But I don't know anything about gardening."),
     ("M", "Don't worry. Experienced members are happy to teach beginners. Why don't you join me this "
           "Saturday and see how it works?"),
     ("W", "")])

q(15, 2, 4, [
    ('q', "다음 상황 설명을 듣고, Olivia가 Andy에게 할 말로 가장 적절한 것을 고르시오."),
    ('speaker', "Olivia:"),
    ('ch', ["Let's practice the presentation together tomorrow.",
            "You'd better choose a more interesting topic.",
            "How about dividing the research among our members?",
            "Why don't we replace some of the text with pictures?",
            "We need to ask the teacher to extend the deadline."], 1)],
    [("M", "Olivia and Andy are preparing a group presentation on ocean pollution for their science class. "
           "Andy has done a lot of research and made the slides. Olivia looks through them and notices that "
           "each slide is filled with long sentences and small letters. She thinks the classmates will find "
           "it hard to read the slides and listen to the speaker at the same time. She also knows that "
           "Andy has collected many powerful photos of plastic waste in the sea, but he hasn't used them. "
           "So Olivia wants to suggest to Andy that they show the photos instead of some of the long "
           "sentences. In this situation, what would Olivia most likely say to Andy?")])

q(16, 2, 3, [
    ('q', "여자가 하는 말의 주제로 가장 적절한 것은?"),
    ('ch', ["ways animals communicate with each other",
            "reasons why some animals live in large groups",
            "how different animals use tools to get food",
            "the importance of protecting wild habitats",
            "differences in intelligence between birds and mammals"], 1)],
    [("W", "Good morning, students. Last time, we talked about how animals find their way home. Today, "
           "we're going to look at how different animals use tools to get food. First, crows are famous for "
           "this. Some crows bend sticks into hooks and use them to pull insects out of holes in trees. "
           "Next, sea otters float on their backs and place a flat stone on their chests. Then they smash "
           "shellfish against the stone to break them open. Chimpanzees also use tools. They push thin "
           "sticks into termite mounds and pull them out covered with termites to eat. Finally, some "
           "octopuses collect coconut shells and use them as shelters while they hunt. As you can see, "
           "tool use is not limited to humans. Now, let's watch a short video.")])

q(17, 2, 5, [
    ('q', "언급된 동물이 <u>아닌</u> 것은?"),
    ('ch', ["crows", "sea otters", "chimpanzees", "octopuses", "elephants"], 3)])

# =============================================================== 독해 18–45
q(18, 2, 2, [
    ('q', "다음 글의 목적으로 가장 적절한 것은?"),
    ('letter', ["Dear Riverside Residents,",
                "I am Daniel Brooks, the director of the Riverside Public Library. Over the past year, many "
                "of you have told us that our current opening hours do not fit your schedules. Many of you work "
                "until late on weekdays. To better "
                "serve our community, "
                "we are considering changing our hours starting next spring. Before making a final "
                "decision, however, we want to hear directly from you. Please take a few minutes to fill out "
                "the short survey on our website and let us know which hours would work best for you. The "
                "survey will be open until March 15. Your opinions will play a key role in shaping the "
                "library's future.",
                "Sincerely,", "Daniel Brooks"]),
    ('ch', ["도서관 자원봉사자 모집을 안내하려고",
            "도서관 운영 시간 변경에 대한 의견을 요청하려고",
            "새로 도입된 도서 대출 서비스를 홍보하려고",
            "도서관 리모델링 공사 지연에 대해 사과하려고",
            "독서 프로그램 참가 신청 마감을 공지하려고"], 1, "tight")])

q(19, 2, 1, [
    ('q', "다음 글에 드러난 Ethan의 심경 변화로 가장 적절한 것은?"),
    ('p', "The trail had disappeared beneath a thick layer of fallen leaves. Ethan stopped and looked around, "
          "but every tree seemed exactly like the one before it. The sun was sinking fast, and his phone showed "
          "no signal. He tried to remember which way the stream had been, but the sound of water was gone. His "
          "heart began to pound as he called out again and again. Then, through a gap in the trees, he noticed "
          "a faint orange glow. He walked toward it and soon found himself at the edge of the campground, where "
          "his friends were waving at him by the fire. Ethan let out a long breath and smiled."),
    ('emo', [("anxious", "relieved"), ("bored", "excited"), ("proud", "ashamed"),
             ("hopeful", "disappointed"), ("calm", "frustrated")])])

q(20, 2, 5, [
    ('q', "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?"),
    ('p', "When scientists share their findings with the public, they often feel pressure to present a clean "
          "and confident story. Yet "
          "science rarely works that way. Most results come with limits: a small sample, a short study "
          "period, or effects that appear only under certain conditions. When these limits are hidden, the "
          "public is set up for confusion. A finding that is later revised looks like a failure, and people "
          "begin to suspect that scientists cannot be trusted. Being honest about uncertainty does the "
          "opposite. It shows how knowledge is built step by step and prepares people for conclusions "
          "that may change. Rather than weakening trust, openly "
          "stating what is not yet known gives the public a more accurate picture of science and a stronger "
          "reason to rely on it."),
    ('fn', "* revise: 수정하다"),
    ('ch', ["과학자는 연구 결과를 대중 매체에 신속히 공개해야 한다.",
            "과학 교육은 실험과 탐구 활동 중심으로 이루어져야 한다.",
            "과학 기사는 전문 용어의 사용을 최소화해야 한다.",
            "연구자는 동료 평가를 거친 결과만을 인용해야 한다.",
            "과학 정보를 전달할 때 불확실성을 솔직히 밝혀야 한다."], 1, "tight")])

q(21, 2, 3, [
    ('q', "밑줄 친 <u>feeding the scale instead of the animal</u>이 다음 글에서 의미하는 바로 가장 적절한 것은?"),
    ('p', "When a measure becomes a target, it often stops being a good measure. Consider a hospital that is "
          "judged by how quickly patients are seen after arriving at the emergency room. At first, the "
          "waiting time is a useful signal of how well the hospital is working. But once managers are "
          "rewarded for short waiting times, the number itself becomes the goal. Staff may greet patients "
          "quickly and record that they have been ‘seen,’ even though real treatment begins hours later. "
          "The figures improve, while the experience of patients stays the same or even gets worse. Similar "
          "patterns appear in schools that focus only on test scores and in companies that count the "
          "number of calls handled per hour. In each case, people start <u>feeding the scale instead of the "
          "animal</u>. The lesson is not that measurement is useless, but that every number is only a "
          "partial window onto what we truly care about, and it must be read with that in mind."),
    ('fn', "* emergency room: 응급실"),
    ('ch', ["ignoring numbers that conflict with personal experience",
            "relying on outside experts to evaluate their performance",
            "improving the indicator instead of what it reflects",
            "measuring progress too often to notice meaningful change",
            "setting goals that are too ambitious to be achieved"], 1)])

q(22, 2, 1, [
    ('q', "다음 글의 요지로 가장 적절한 것은?"),
    ('p', "Most of us treat boredom as a problem to be solved, and with a smartphone in our pocket, the "
          "solution is always at hand. Yet psychologists have found that boredom may serve a valuable "
          "purpose. In one study, participants who first completed a dull task, such as copying numbers "
          "from a phone book, later came up with more creative uses for everyday objects than those who had "
          "not been bored. Researchers suggest that when the outside world offers little stimulation, the "
          "mind begins to wander and search for something more interesting. During this wandering, it "
          "connects ideas that normally remain apart, and new possibilities emerge. Boredom, in other words, "
          "is a signal that pushes us to seek novelty, and that search can lead to original thinking. Many "
          "great ideas, in fact, have reportedly arrived during long walks or quiet train rides. The "
          "problem is that we rarely allow ourselves to stay bored long enough for this process to unfold. "
          "By reaching for our devices at the first sign of dullness, we may be cutting off one of the most "
          "natural sources of creativity we have."),
    ('fn', "* stimulation: 자극   ** novelty: 새로움"),
    ('ch', ["지루함은 창의적 사고를 촉진하는 계기가 될 수 있다.",
            "지루함을 피하려면 다양한 취미 활동이 필요하다.",
            "디지털 기기는 업무 집중력 향상에 도움을 준다.",
            "창의성은 타고난 재능보다 꾸준한 노력으로 길러진다.",
            "휴식 시간을 늘리면 학습의 효율이 높아진다."], 1)])

q(23, 2, 4, [
    ('q', "다음 글의 주제로 가장 적절한 것은?"),
    ('p', "We usually think of forgetting as a failure of memory, a sign that something has gone wrong. "
          "However, a growing body of research suggests that forgetting is an essential part of how memory "
          "works well. The brain does not store experiences in order to keep a perfect record of the past; "
          "it stores them to guide future behavior. If we remembered every detail of every day, we would "
          "struggle to separate what matters from what does not. Imagine trying to recall where you parked "
          "your car today while every past parking spot competes for attention. By letting go of outdated "
          "or unimportant information, the brain makes room for what is useful and allows us to form general "
          "rules from specific events. In a world that keeps changing, a memory that held on to everything "
          "would quickly become a burden. Forgetting, then, is not simply a loss but a process that helps "
          "us adapt."),
    ('fn', "* outdated: 시대에 뒤떨어진"),
    ('ch', ["methods of improving long-term memory by repetition",
            "negative effects of stress on the formation of memory",
            "differences between human memory and computer storage",
            "adaptive function of forgetting in human memory",
            "reasons why childhood memories are often inaccurate"], 1)])

q(24, 3, 2, [
    ('q', "다음 글의 제목으로 가장 적절한 것은? [3점]"),
    ('p', "Every map is a simplification. To be useful, a map must leave out far more than it includes. A "
          "subway map, for example, ignores the actual distances between stations and the curves of the "
          "tracks, showing only the order of stops and the points where lines connect, which is all most "
          "passengers need. A road map may show "
          "highways in bold colors while omitting hills, forests, and small paths. These choices are not "
          "mistakes; they are what make maps readable. Yet they also mean that maps are never neutral. "
          "Someone must decide what deserves to appear and what can safely disappear, and those decisions "
          "reflect particular purposes and values. A map designed for tourists highlights attractions and "
          "shopping streets, while a map of the same city made for emergency planners emphasizes hospitals "
          "and evacuation routes. Even the choice of which region to place at the center of a world map can "
          "shape how people see their place in the world. When we look at a map, then, we are not seeing the "
          "world as it is but the world as someone has chosen to present it. Reading maps wisely means asking "
          "what they leave out."),
    ('fn', "* omit: 생략하다   ** evacuation: 대피"),
    ('ch', ["The History of Map-Making: From Clay to Satellites",
            "Every Map Is a Choice: The Hidden Selectivity of Maps",
            "Can Digital Maps Replace Our Sense of Direction?",
            "Accurate Maps, Better Decisions: The Power of Data",
            "Why Mapmakers Prefer Smaller Scales to Larger Ones"], 1)])

q(25, 2, 5, [
    ('q', "다음 도표의 내용과 일치하지 <u>않는</u> 것은?"),
    ('fig', "fig_r25", 292.8, 198.6),
    ('p', "The graph above shows the results of surveys in which teenagers aged 13 to 18 were asked to choose "
          "their main source of news in 2016 and in 2026. Respondents could choose only one source. ① In both 2016 and 2026, social media was the most preferred "
          "news source among teenagers, and its percentage increased by 13 percentage points over the ten "
          "years. ② The percentage of teenagers who preferred video platforms in 2026 was more than one and a "
          "half times that in 2016, while the percentage of those who preferred news websites decreased by "
          "half. ③ News websites, which ranked second in 2016, fell to third place in 2026, behind social "
          "media and video platforms, which together accounted for three quarters of all responses. ④ The percentage of teenagers who preferred TV in 2026 was half of that "
          "in 2016, and TV was less preferred than news websites in both years. ⑤ Print newspapers were the "
          "least preferred news source in both years, and the gap between their percentages in 2016 and 2026 "
          "was more than 5 percentage points.")])

q(26, 2, 3, [
    ('q', "Maria Sibylla Merian에 관한 다음 글의 내용과 일치하지 <u>않는</u> 것은?"),
    ('p', "Maria Sibylla Merian was born in Frankfurt, Germany, in 1647. Her stepfather, a still-life painter, "
          "taught her how to draw and paint, and from an early age she showed a strong interest in insects. "
          "At a time when many people believed that insects came from mud, she carefully observed "
          "caterpillars and recorded how they changed into butterflies and moths. In 1679, she published a "
          "book on caterpillars with detailed illustrations of their life cycles. In 1699, Merian traveled "
          "to Suriname in South America with her daughter to study the insects and plants "
          "there. Although illness forced her to return home two years later, she used her observations to "
          "produce her most famous work, <i>Metamorphosis insectorum Surinamensium</i>, in 1705. Her portrait "
          "later appeared on a German banknote."),
    ('fn', "* still-life: 정물(화)의   ** metamorphosis: 변태"),
    ('ch', ["독일의 Frankfurt에서 태어났다.",
            "의붓아버지에게서 그림 그리는 법을 배웠다.",
            "1699년에 아들과 함께 Suriname으로 떠났다.",
            "1705년에 가장 유명한 저서를 출간했다.",
            "그녀의 초상화가 독일 지폐에 실렸다."], 1, "tight")])

q(27, 2, 4, [
    ('q', "2027 Riverside Photo Contest에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?"),
    ('notice', "2027 Riverside Photo Contest", [
        ('t', "Show us the beauty of our river! The theme of this year’s contest is <i>Life by the River</i>."),
        ('kv', "Deadline", "June 30, 2027"),
        ('kv', "Participants", "Riverside City residents of all ages"),
        ('h', "Submission Guidelines"),
        ('b', "Each person may submit up to two photos."),
        ('b', "Photos must be taken in 2027."),
        ('b', "Each photo must have a title of no more than 10 words."),
        ('b', "Send your photos by email to photo@riverside*city.org."),
        ('h', "Judging"),
        ('b', "Photos will be judged on creativity and connection to the theme."),
        ('h', "Prizes"),
        ('b', "First Place: $300 gift card"),
        ('b', "The winning photos will be displayed at City Hall in August."),
        ('r', "※ For more information, visit www.riverside*photo.org.")]),
    ('ch', ["주제는 강가에서의 삶이다.",
            "모든 연령의 Riverside City 주민이 참가할 수 있다.",
            "1인당 최대 두 장의 사진을 제출할 수 있다.",
            "2026년에 촬영한 사진도 제출할 수 있다.",
            "수상작은 8월에 시청에 전시될 것이다."], 1)])

q(28, 2, 2, [
    ('q', "Weekend Kayak Tour에 관한 다음 안내문의 내용과 일치하는 것은?"),
    ('notice', "Weekend Kayak Tour", [
        ('t', "Paddle along the calm waters of Lake Silva and enjoy the beautiful scenery with our "
              "experienced guides!"),
        ('kv', "When", "Every Saturday and Sunday, May to September"),
        ('h', "Tour Types"),
        ('tbl', ["Tour", "Price", "Details"],
         [["Morning", "$35", "2 hours (snacks included)"],
          ["Sunset", "$45", "2.5 hours (photo package included)"],
          ["Private", "$80", "2 hours (up to 4 people)"]]),
        ('h', "Notes"),
        ('b', "Participants must be at least 12 years old."),
        ('b', "Life jackets are provided free of charge."),
        ('b', "Each tour group is limited to 10 people."),
        ('b', "Tours start at the Lake Silva Boat Dock."),
        ('b', "Free parking is available near the dock."),
        ('b', "Reservations must be made at least two days in advance."),
        ('b', "Bring a change of clothes and sunscreen."),
        ('r', "※ Tours may be canceled due to bad weather."),
        ('r', "※ For more information, visit www.lakesilva*kayak.com.")]),
    ('ch', ["모든 투어는 평일에만 운영된다.",
            "선셋 투어에는 사진 패키지가 포함된다.",
            "10세 이상이면 참가할 수 있다.",
            "구명조끼는 유료로 대여해야 한다.",
            "투어 당일에 예약할 수 있다."], 1)])

q(29, 2, 3, [
    ('q', "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?"),
    ('p', "Many animals communicate, but few do so with the precision of the honeybee. When a forager bee "
          "discovers a rich source of food, she returns to the hive and performs a ‘waggle dance’ in the dark "
          "hive that "
          "① <u>informs</u> her sisters where to find it. The angle of the dance relative to the vertical "
          "shows the direction of the food in relation to the sun, and the length of the waggle run "
          "indicates ② <u>how</u> far away the source is. What makes this system remarkable is "
          "③ <u>what</u> the information it carries can be used even when the sun is hidden behind clouds, "
          "because bees can detect patterns of polarized light in the sky that are invisible to human eyes. "
          "Other bees follow the dancer "
          "closely, ④ <u>sensing</u> the vibrations of her body, and then fly off in search of the food. "
          "Researchers who have decoded the dance can predict where the bees will go, a fact that shows "
          "how much information ⑤ <u>is</u> packed into a few seconds of movement. Few other animals are known "
          "to share such detailed directions with members of their group."),
    ('fn', "* forager: 먹이를 찾아다니는 동물   ** polarized: 편광된")])

q(30, 3, 4, [
    ('q', "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은? [3점]"),
    ('p', "Habits form when a behavior is repeated in a stable context until it no longer requires "
          "conscious thought. This is why changes in our surroundings can be a powerful "
          "① <u>opportunity</u> for changing behavior. When people move to a new city, start a new job, or "
          "even rearrange their furniture, the cues that once triggered their old habits are "
          "② <u>disrupted</u>. In one study, students who transferred to a new university were more likely "
          "to change their exercise habits than students who stayed, but only when the new environment was "
          "③ <u>different</u> enough from the old one. Researchers call this the ‘habit discontinuity’ "
          "effect. It suggests that the moment of a move is an ideal time to build healthier routines, "
          "because the automatic pull of past behavior is temporarily ④ <u>strengthened</u>. People who "
          "wish to change a habit can therefore benefit from timing their efforts to coincide with natural "
          "transitions in their lives. Those who wait until everything has settled, by contrast, may find "
          "that new cues quickly become attached to the same old behaviors, making change "
          "⑤ <u>difficult</u> again."),
    ('fn', "* discontinuity: 불연속성")])

q(31, 2, 1, [
    ('p0', "Engineers who design bridges and tall buildings have long known that strength alone is not "
           "enough. A structure that is completely rigid may seem secure, but when it is hit by strong winds "
           "or an earthquake, it has no way to absorb the energy, and it can crack or collapse. That is why "
           "many modern skyscrapers are built to sway slightly, sometimes by more than a meter at the top. Some "
           "buildings even rest on rubber pads that let them shift gently as the ground moves. Bridges, too, "
           "include joints that allow them to expand and contract with changes in "
           "temperature. The same principle can be found in nature. A tall tree bends in a storm rather "
           "than standing stiffly against it, and the stems of grasses survive winds that would break a "
           "dry stick. Rigid materials, by contrast, often fail suddenly and completely. Even our own bones are not perfectly hard; they contain materials that let them bend "
           "slightly under pressure. In each case, <blank:30> rather than rigidity is what allows a system "
           "to endure. Survival under stress, it seems, depends less on resisting every force than on "
           "adjusting to it without losing overall form."),
    ('fn', "* contract: 수축하다"),
    ('ch', ["flexibility", "complexity", "stability", "efficiency", "visibility"], 2)])

q(32, 3, 5, [
    ('p0', "Why do some people stay calm when plans fall apart while others feel overwhelmed? Part of the "
           "answer lies in how they explain events to themselves. Psychologists have found that people who "
           "cope well with setbacks tend to view problems as temporary and specific rather than permanent "
           "and general. Others see one failure as proof of a lasting flaw. When a project fails, they think, ‘This approach did not work this time,’ not ‘I "
           "am bad at everything.’ This way of thinking does not deny the problem, but it limits its reach, "
           "so that a single failure does not spread into every area of life. Importantly, this habit can be "
           "learned. In training programs, participants practice noticing their automatic explanations and "
           "questioning whether they are accurate. Over time, they become better at separating what "
           "happened from what it means about them. People trained in this way tend to recover from "
           "disappointments more quickly and give up less easily. The key to resilience, then, may lie not in avoiding "
           "difficulties but in learning to <blank:44>. [3점]"),
    ('ch', ["predict problems before they occur",
            "rely on others to solve their problems",
            "hide negative emotions from the people around them",
            "set higher goals after each small success",
            "interpret setbacks in a limited and changeable way"], 1)])

q(33, 2, 2, [
    ('p0', "In many sports, coaches spend hours analyzing videos of their own team. But some of the most "
           "valuable insights come from studying how other teams fail. Watching an opponent’s mistakes helps "
           "players recognize patterns that are hard to see in their own performance, because they are not "
           "emotionally involved. The same holds true outside sports. In medicine, hospitals that share "
           "reports of errors with one another reduce the number of repeated mistakes, since each hospital "
           "can learn from problems it has never experienced itself. Airlines have created systems in which "
           "pilots can report near-accidents without fear of punishment, and the information is passed on "
           "to crews around the world. Mountain climbers study accounts of failed expeditions for the same "
           "reason, hoping to avoid the errors that others paid for dearly. These practices rest on a simple idea: an organization that learns "
           "only from its own experience will learn slowly, because each lesson must be paid for directly. "
           "By contrast, an organization that <blank:40> multiplies its opportunities to improve without "
           "having to suffer every failure firsthand."),
    ('ch', ["focuses on its own past successes",
            "treats the failures of others as a source of learning",
            "avoids sharing information with its competitors",
            "punishes mistakes to prevent them from happening again",
            "relies on experts from outside its field"], 1)])

q(34, 3, 4, [
    ('p0', "Early in the history of the printed book, readers often treated their volumes as places for "
           "conversation. They wrote comments in the margins, argued with the author, corrected errors, and "
           "added notes for future readers. A single copy might pass through many hands, gathering layers "
           "of responses over the years. Some readers even copied passages from other books into the margins, "
           "linking one text to another. "
           "Collectors in later centuries often erased such notes, unaware that they were destroying valuable "
           "evidence. Today, such marks are often seen as damage, and libraries ask "
           "readers to keep books clean. Yet historians value these old annotations because they reveal how "
           "people actually read, what puzzled them, and which ideas excited or angered them. A printed "
           "text, in this sense, was never finished when it left the printer. Its meaning continued to grow "
           "as readers responded to it, and those responses became part of the object itself. To understand "
           "a book from the past, then, we must look beyond the words the author wrote and consider the "
           "book as <blank:44>. [3점]"),
    ('fn', "* annotation: 주석"),
    ('ch', ["a product designed for a single owner",
            "a symbol of wealth and social status",
            "an exact record of the author’s original intention",
            "an ongoing exchange between the text and its readers",
            "a historical object that must be preserved untouched"], 1)])

q(35, 2, 3, [
    ('q', "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?"),
    ('p', "As cities grow denser and land becomes more expensive, planners are looking upward. Rooftops that "
          "once sat empty are now being turned into valuable spaces. From New York to Singapore, the idea of "
          "the green roof has spread rapidly. ① Green roofs, covered with soil and "
          "plants, absorb rainwater that would otherwise flood streets and sewers during heavy storms. "
          "② They also act as insulation, keeping buildings cooler in summer and warmer in winter, which "
          "lowers energy use. ③ Many older buildings, however, were designed with flat roofs simply because "
          "they were cheaper to build than sloped ones. ④ In addition, the plants on these roofs provide "
          "habitats for birds and insects, bringing a bit of nature back into dense urban areas. ⑤ Some "
          "cities now offer tax benefits to building owners who install green roofs, hoping to spread "
          "these advantages across entire neighborhoods and improve the quality of urban life."),
    ('fn', "* insulation: 단열")])

q(36, 2, 2, [
    ('box', [('p', "Long before the invention of refrigerators, people developed clever ways to keep food "
                   "from spoiling. Many of these methods worked by removing the conditions, such as warmth and "
                   "moisture, that bacteria need in order to grow.")]),
    ('pl', "(A)", "Salt worked in a similar way. When food was packed in salt, the salt drew water out of "
                  "it, creating an environment just as unfriendly to bacteria. Salted fish and meat could last for "
                  "many months, even on long sea voyages far from any port."),
    ('pl', "(B)", "One of the oldest methods was drying. By leaving fruit, fish, or meat in the sun and "
                  "wind for several days, people reduced the amount of water in the food, and without enough "
                  "moisture, most bacteria simply could not survive. Dried food was also light and easy to carry."),
    ('pl', "(C)", "These voyages, in fact, depended heavily on preserved food. Without salted and dried "
                  "supplies, sailors could not have crossed oceans, and the age of exploration might have "
                  "unfolded very differently. Preservation, in other words, did more than feed people; it helped "
                  "shape history."),
    ('fn', "* voyage: 항해"),
    ('ord', ORD3)])

q(37, 3, 5, [
    ('box', [('p', "When we listen to someone speak, we do not simply wait for each word to arrive and then "
                   "work out what it means. Our brains are constantly predicting what will come next, often "
                   "several words ahead.")]),
    ('pl', "(A)", "Such guesses, however, can sometimes lead us astray. When a speaker says something "
                  "unexpected, we may hear what we predicted rather than what was actually said. Many "
                  "misunderstandings in everyday life begin in exactly this way, a reminder that perception is "
                  "partly an act of construction rather than simple recording."),
    ('pl', "(B)", "Because of this, we often understand a sentence before it is even finished. In a noisy "
                  "room, we may fill in words we did not clearly hear without even noticing that we have "
                  "done so. This ability makes conversation fast and efficient, even in difficult conditions such as crowded cafés."),
    ('pl', "(C)", "This prediction happens at many levels. Based on the topic and the speaker’s tone, we "
                  "expect certain kinds of words, and as a sentence unfolds, the range of possible endings "
                  "narrows quickly. By the time a speaker says ‘I’d like a cup of,’ most listeners have already "
                  "guessed the next word. [3점]"),
    ('fn', "* astray: 길을 잃고"),
    ('ord', ORD3)])

q(38, 2, 4, [
    ('box', [('p', "That figure then serves as an anchor against which every later offer is judged.")]),
    ('p', "In negotiations, people often believe that the side that waits to hear the other’s offer has an "
          "advantage, since it can learn something before revealing its own position. ( ① ) Research, however, suggests that the opposite is frequently true. ( ② ) The "
          "person who speaks first tends to set the terms of the discussion in his or her favor, because the "
          "other side begins thinking within the range that has been introduced. ( ③ ) "
          "Suppose a seller of a used car opens by asking for $12,000, even though similar cars sell for "
          "about $9,000. ( ④ ) Even a buyer who knows the price is too high will usually make a "
          "counteroffer closer to $12,000 than he or she would have otherwise, and the final price often ends "
          "up well above $9,000. ( ⑤ ) For this reason, "
          "experienced negotiators prepare carefully before a meeting so that they can make an ambitious "
          "but realistic first offer, rather than waiting for the other side to name a number. Those who "
          "receive a bold first offer are advised to respond with a strong number of their own."),
    ('fn', "* anchor: 닻, 기준점   ** counteroffer: 수정 제안")])

q(39, 3, 3, [
    ('box', [('p', "As a result, the same color can look entirely different depending on what surrounds "
                   "it.")]),
    ('p', "We tend to assume that the color we see belongs to the object itself, just like its size or shape. ( ① ) In reality, color "
          "is something the brain constructs from the light that reaches our eyes, and that light changes "
          "with the time of day and the weather. ( ② ) Moreover, the brain does not judge the light from "
          "each object on its own; it compares it with the light coming from nearby areas. ( ③ ) Such differences can be "
          "striking: a gray square placed on a black background looks lighter than an identical square on a "
          "white one. "
          "( ④ ) Artists have long used this effect, placing colors side by side so that each makes the "
          "other appear more vivid. Designers apply the same principle when choosing background colors for "
          "logos and websites. ( ⑤ ) Understanding that color depends on context helps explain why a "
          "shirt that looked perfect in the store may seem dull at home, where it is surrounded by different "
          "colors and lit by different light. [3점]"),
    ('fn', "* vivid: 선명한")])

q(40, 2, 1, [
    ('q', "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?"),
    ('box', [('p', "In a series of experiments, researchers asked participants to assemble simple storage "
                   "boxes, fold paper animals, or build small models from kits. Afterward, the participants "
                   "were asked how much they would be willing to pay for their own creations. Surprisingly, "
                   "they valued their own work far more highly than identical items assembled by others, "
                   "and in some cases they valued their amateur creations nearly as much as products made "
                   "by experts. The effect disappeared, however, when participants built something and then "
                   "were asked to take it apart, or when they failed to complete the task. Effort alone, it seems, "
                   "was not enough to create the effect. In another study, children who built a simple toy were "
                   "more reluctant to trade it away than children who had received the same toy already "
                   "assembled. Researchers "
                   "concluded that the extra value came not from the object itself but from the effort "
                   "invested in it and the sense of accomplishment that followed. This finding helps "
                   "explain why many companies now invite customers to take part in creating products, "
                   "whether by designing their own sneakers, decorating their own cakes, or assembling furniture at "
                   "home."),
             ('fn', "* assemble: 조립하다")]),
    ('arrow',),
    ('summary', "People tend to <ublank:(A)> things they have made themselves, but only when their effort "
                "ends in <ublank:(B)> rather than being undone or left unfinished."),
    ('ab', [("overvalue", "success"), ("overvalue", "failure"), ("ignore", "success"),
            ("ignore", "failure"), ("imitate", "praise")])])

# 41–42 장문
P41 = [
    "When students study for an exam, they usually choose methods that make learning feel smooth and easy. "
    "They reread their notes and highlight key sentences again and again. These "
    "strategies create a pleasant sense of familiarity, and students often leave a study session feeling "
    "(a) <u>confident</u> that they have mastered the content. Yet this "
    "feeling can be misleading. Familiarity is not the same as understanding, and material that seems easy "
    "to recognize on the page may be surprisingly hard to recall during a test.",
    "Psychologists use the term ‘desirable difficulties’ to describe learning conditions that slow down "
    "progress in the short term but (b) <u>improve</u> long-term retention. One example is retrieval "
    "practice, in which learners close the book and try to recall information from memory. This effort "
    "feels harder than rereading, but each act of "
    "retrieval strengthens the memory, making it easier to access later. Another example is spacing, or "
    "spreading study sessions out over several days instead of (c) <u>concentrating</u> them in a single "
    "evening. The effort needed to rebuild partly forgotten memories deepens learning.",
    "The challenge is that these methods rarely feel effective while they are being used. Because they "
    "involve struggle, learners often (d) <u>misjudge</u> them as unproductive and return to easier "
    "strategies. When students understand that effort is a sign of learning "
    "rather than a sign of failure, they become more willing to (e) <u>avoid</u> the challenges that make "
    "knowledge last.",
]
q(41, 3, 2, [
    ('q', "윗글의 제목으로 가장 적절한 것은? [3점]"),
    ('ch', ["Why Rereading Is the Most Reliable Way to Learn",
            "Learning That Lasts: Why Struggle Pays Off",
            "The Hidden Cost of Studying with Your Friends",
            "Forget Less by Studying Less Often",
            "How Teachers Can Make Learning Feel Easier"], 1)])
q(42, 2, 5, [
    ('q', "밑줄 친 (a)～(e) 중에서 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?"),
    ('ch', ABCDE, 5)])

# 43–45 장문
P43 = {
    "(A)": "Leo had never liked spending weekends at his grandfather’s farmhouse, where the days seemed to "
           "stretch on forever. On the first Saturday of the summer, Grandpa Walter found Leo lying on the sofa, "
           "staring at his phone. “Come with me,” Walter said, holding up an old toolbox. “I need a helper.” "
           "Leo sighed, but (a) <u>he</u> put down the phone and followed his grandfather out to the barn. "
           "“We’re going to build a birdhouse,” Walter announced. “The bluebirds will be back soon.”",
    "(B)": "At first, Leo held the boards while his grandfather measured and cut. But soon Walter handed him "
           "the hammer. “Your turn,” he said. Leo’s first nail bent sideways, and the second one missed "
           "completely. Frustrated, (b) <u>he</u> threw the hammer onto the workbench. Walter only chuckled. "
           "“My first birdhouse fell apart in the rain,” he said. “Nails are like people. Each one needs a "
           "little patience.” Leo picked up the hammer again, this time tapping gently before striking "
           "harder. The nail slid straight into the wood, and he couldn’t help grinning.",
    "(C)": "On Thursday morning, Leo ran into the kitchen, nearly knocking over a chair. “Grandpa! They’re "
           "here!” Walter put down (d) <u>his</u> coffee and followed his grandson outside. A pair of "
           "bluebirds was flying in and out of the small round door, carrying twigs and grass. Leo watched "
           "them for a long time without saying a word. That evening, he called his mother. “Can I stay here "
           "for the rest of the summer?” (e) <u>he</u> asked. On the other end of the line, she laughed in "
           "surprise.",
    "(D)": "By late afternoon, the birdhouse was finished. It was a little crooked, and one side was painted "
           "a brighter blue than the other, but Leo thought it was perfect. Together they carried it to the "
           "old oak tree by the field. Walter held the ladder while Leo climbed up and fastened it to a "
           "strong branch. When (c) <u>he</u> came down, his grandfather put a hand on his shoulder. “Now we "
           "wait,” Walter said. “Good things usually take their time.” For the next few days, Leo checked "
           "the birdhouse every morning, but it remained empty, and he began to wonder if any birds would ever "
           "come.",
}
q(43, 2, 1, [
    ('q', "주어진 글 (A)에 이어질 내용을 순서에 맞게 배열한 것으로 가장 적절한 것은?"),
    ('ord', ORD4)])
q(44, 2, 4, [
    ('q', "밑줄 친 (a)～(e) 중에서 가리키는 대상이 나머지 넷과 <u>다른</u> 것은?"),
    ('ch', ABCDE, 5)])
q(45, 2, 1, [
    ('q', "윗글에 관한 내용으로 적절하지 <u>않은</u> 것은?"),
    ('ch', ["Leo는 할아버지의 농장에서 주말을 보내는 것을 좋아했다.",
            "Walter는 처음 만든 새집이 비에 망가졌다고 말했다.",
            "Leo가 사다리에 올라가 새집을 나뭇가지에 고정했다.",
            "며칠 동안 새집은 비어 있었다.",
            "Leo는 어머니에게 여름 내내 머물러도 되는지 물었다."], 1, "tight")])

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
