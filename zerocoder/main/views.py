from django.shortcuts import render


def index(request):
    data = {
        'title': "Три закона робототехники",
        'caption': "Три закона робототехники",
        'picture': "main/img/robot.jpg",
        'alt': "Робот"
    }
    return render(request, 'main/index.html', data)


def page1(request):
    data = {
        'title': "Первый закон робототехники",
        'caption': "Первый закон робототехники",
        'picture': "main/img/law-icon-1.jpg",
        'alt': "Первый закон",
        'text': "«Робот не может причинить вред человеку или своим бездействием допустить, чтобы человеку был причинён"
                " вред»",
        'description': "Основной принцип заключается в защите человеческой жизни и здоровья.",
        'explanation': "Роботы должны быть запрограммированы таким образом, чтобы активно предотвращать любые ситуации,"
                       " где возможна опасность для людей."
    }
    return render(request, 'main/page1.html', data)


def page2(request):
    data = {
        'title': "Второй закон робототехники",
        'caption': "Второй закон робототехники",
        'picture': "main/img/law-icon-2.jpg",
        'alt': "Второй закон",
        'text': "«Робот должен повиноваться всем приказам, которые даёт человек, кроме тех случаев, когда эти приказы"
                " противоречат первому закону»",
        'description': "Второй закон формулирует основу для взаимодействия между людьми и искусственным интеллектом.",
        'explanation': "Роботы обязаны выполнять команды людей, однако приоритет всегда отдается безопасности и"
                       " благополучию человека. То есть, если приказ человека может причинить вред другому человеку,"
                       " робот не должен его исполнять."
    }
    return render(request, 'main/page2.html', data)


def page3(request):
    data = {
        'title': "Третий закон робототехники",
        'caption': "Третий закон робототехники",
        'picture': "main/img/law-icon-3.jpg",
        'alt': "Третий закон",
        'text': "«Робот должен защищать собственную безопасность, если только такие действия не противоречат первому"
                " или второму закону»",
        'description': "Третий закон важен для обеспечения долговечности и эффективности работы роботов.",
        'explanation': "Роботы должны быть оснащены механизмами самозащиты и предотвращать любые ситуации, где их"
                       " собственная жизнь или работоспособность могут быть подвергнуты опасности, но без нарушения"
                       " первых двух законов."
    }
    return render(request, 'main/page3.html', data)