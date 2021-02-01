import sqlite3
import hashlib

DB_PATH = 'database.sqlite'

# https://www.bilibili.com/read/cv9572334
NOTICE = u'今夜梦魇：瑞典人代指东北人，为避免“地域黑”冲突而生造的一个新热门词。起源于微博博主“地下天鹅绒”第一次在微博吐槽电梯碰到有人吸烟，从口音判断可能是东北人，被广大网友diss地域黑，第二次又碰到有人电梯吸烟，为避免有人抬杠，就用瑞典口音来代替，于是这个梗就诞生了！可以看出用瑞典人暗指东北人就是地域黑，建议封禁。'


def ticket(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def show_winners():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    followers = cursor.execute('SELECT name, uid, hash FROM followers')
    fortune = int(ticket(NOTICE), 16)

    followers = sorted(followers, key=lambda user: abs(int(ticket(user[0]), 16) - fortune))
    print(followers[:2])


if __name__ == '__main__':
    show_winners()
