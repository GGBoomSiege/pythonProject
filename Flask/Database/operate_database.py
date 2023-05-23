from learn_sql import db, Student, Teacher, Course, Grade, app

with app.app_context():
    # 增
    # s = []
    #
    # s.append(Student(name='张三', gender='男', phone='12345678910'))
    # s.append(Student(name='李四', gender='男', phone='12345678910'))
    # s.append(Student(name='王五', gender='男', phone='12345678910'))
    # s.append(Student(name='赵六', gender='女', phone='12345678910'))
    # # db.session.add_all(s)
    #
    # s.append(Teacher(name='xx', gender='男', phone='12345678910'))
    # s.append(Teacher(name='yy', gender='女', phone='12345678910'))
    # s.append(Teacher(name='zz', gender='男', phone='12345678910'))
    # # db.session.add_all(s)
    #
    # s.append(Course(course_name='语文', teacher_id=1))
    # s.append(Course(course_name='数学', teacher_id=2))
    # s.append(Course(course_name='英语', teacher_id=3))
    #
    # s.append(Grade(course_id=1, student_id=1, score=100))
    # s.append(Grade(course_id=2, student_id=1, score=90))
    # s.append(Grade(course_id=3, student_id=1, score=80))
    #
    # s.append(Grade(course_id=1, student_id=2, score=70))
    # s.append(Grade(course_id=2, student_id=2, score=75))
    #
    # s.append(Grade(course_id=2, student_id=3, score=60))
    # s.append(Grade(course_id=3, student_id=3, score=65))
    #
    # #
    # # #     # 添加语句
    # # #     # db.session.add(s[1])
    # db.session.add_all(s)
    # db.session.commit()

    # 查
    #     stu = db.session.get(Student,10)
    #     stu = Student.query.get(2)
    #     print(stu.name)
    #
    #     stu = Student.query.all()[6]
    #     print(stu.name)
    #
    #     stu = Student.query.filter_by(id>=6).first()
    #     stu = db.session.query(Student).filter(Student.name=="张三").all()

    # 通过主表关联关系访问
    # stu = db.session.query(Student).filter(Student.id == 2).first()
    # # print(type(stu))
    # for course in stu.courses:
    #     for score in stu.grades:
    #         print(
    #             stu.id, stu.name, stu.gender, stu.phone,
    #             course.course_name, score.score
    #         )
    #
    # print('---------------------------------------------------------')
    #
    # # 通过外键访问
    # stu = db.session.query(Grade).filter(Student.id == 2).all()
    # # print(type(stu))
    # for item in stu:
    #     print(
    #         item.student.id, item.student.name, item.student.gender, item.student.phone,
    #         item.course.course_name, item.score
    #     )

    # 改
    #     stu = db.session.query(Grade).filter(Student.id==2).update({'score':75})
    #     db.session.commit()
    #     print(stu)
    #     stu = db.session.query(Student).all()
    #     for item in stu:
    #         print(item.name,item.gender,item.phone)

    # 删
    #     stu = db.session.query(Student).filter(Student.id==4).delete()
    #     db.session.commit()

    # 多表查询
    course = db.session.query(Course).all()

    stu = db.session.query(Student).all()
    for item in stu:
        print(item.name, item.gender, item.phone)
        item.courses = course
        db.session.add(item)
        db.session.commit()