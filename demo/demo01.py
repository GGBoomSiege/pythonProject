import os

filename='student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统么？y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')

def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001):')
        if not id:
            break
        name=input('请输入姓名:')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入Python成绩:'))
            java=int(input('请输入Java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入！')
            continue
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加?y/n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break

    save(student_list)
    print('学生信息录入完毕！！！')

def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示！')
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                 ))

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查找请输入1,按姓名查找请输入2:')
            if mode=='1':
                id=input('请输入学生ID:')
            elif mode=='2':
                name=input('请输入学生姓名:')
            else:
                print('您的输入有误，请重新输入！')
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer=input('是否要继续查询?y/n')
            if answer=='y' or answer=='Y':
                continue
            break
        else:
            print('暂未保存学生信息！')
            break

def delete():
    while True:
        student_id=input('请输入要删除的学生的ID:')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除！')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息！')
                break
            show()
            anwser=input('是否继续删除?y/n')
            if anwser=='y' or anwser=='Y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        print('暂未保存学生信息！')
        return
    student_id=input('请输入要修改的学生的ID:')
    if student_id!='':
        with open(filename,'w',encoding='utf-8') as wfile:
            for item in student_old:
                d=dict(eval(item))
                if d['id']==student_id:
                    print('找到学生信息，可以修改相关信息！')
                    while True:
                        try:
                            d['name']=input('请输入姓名:')
                            d['english']=int(input('请输入英语成绩:'))
                            d['python']=int(input('请输入Python成绩:'))
                            d['java']=int(input('请输入Java成绩:'))
                            wfile.write(str(d) + '\n')
                            print('修改成功！！！')
                            break
                        except:
                            print('您的输入有误，请重新输入!')
                else:
                    wfile.write(str(d)+'\n')
            answer=input('是否继续修改其他学生信息？y/n')
            if answer=='y' or answer=='Y':
                modify()
    else:
        print('输入的学生ID为空！')
        modify()


def sort():
    pass

def total():
    pass

def show():
    pass

def menu():
    print('============学生信息管理系统===============')
    print("----------------功能菜单------------------")
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出系统')
    print("----------------------------------------")

main()
