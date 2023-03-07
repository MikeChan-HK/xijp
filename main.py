import cgi

# 設置編碼方式為UTF-8，以避免中文亂碼問題
print("Content-Type: text/html;charset=utf-8")
print()

# 讀取HTML表單中的輸入值
form = cgi.FieldStorage()
who = form.getvalue('who', '')
leadership = form.getvalue('leadership', '')

# 計算出結果
out = f'{who}的领导直接关系{leadership}的根本方向、前途命运、最终成败。{who}的领导决定{leadership}的根本性质，只有毫不动摇坚持{who}的领导，{leadership}才能前景光明、繁荣兴盛；否则就会偏离航向、丧失灵魂，甚至犯颠覆性错误。{who}的领导确保{leadership}锚定奋斗目标行稳致远，我们{who}的奋斗目标一以贯之，一代一代地接力推进，取得了举世瞩目、彪炳史册的辉煌业绩。{who}的领导激发建设{leadership}的强劲动力，我们{who}勇于改革创新，不断破除各方面体制机制弊端，为{leadership}注入不竭动力。{who}的领导凝聚建设{leadership}的磅礴力量，{who}坚持{leadership}的群众路线，坚持以人民为中心的发展思想，发展全过程人民民主，充分激发全体人民的主人翁精神'

# 將結果作為回應傳回給HTML頁面
print(f"out={out}")