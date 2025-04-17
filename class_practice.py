import tkinter
import random

class Circle:
    """円を星と見立てて画面に表示
    """

    def __init__(self):
        """コンストラクタでインスタンス変数を定義
        """
        self.x = random.randint(0, 600)
        self.y = random.randint(0, 400)
        self.speed = random.randint(1, 6)
        # 速度の数値を6で割り2を掛ける事で速度最大の時は白くなり速度が遅い程黒くなるように
        # RGBそれぞれ2桁の16進数に書式を指定している
        self.color = f'#{int(self.speed/6*255):02x}{int(self.speed/6*255):02x}{int(self.speed/6*255):02x}'
        # 個別の円のIDを受ける変数を設定
        self.id = None

    def draw(self):
        """円を描画
        """
        self.id = canvas.create_oval(self.x-3,
                                     self.y-3,
                                     self.x+3,
                                     self.y+3,
                                     fill=self.color,
                                     width=0)

    def move(self):
        """Circleが持つX座標を速度の値だけ減算し、円が左に移動するようにする
        """
        self.x -= self.speed
        if self.x < 0:
            self.x = 600  # 画面左端までいったら右端へ
        canvas.coords(self.id,
                      self.x-3,
                      self.y-3,
                      self.x+3,
                      self.y+3)

def main():
    """一定間隔で何度も実行するようにする。
    """
    for star in stars:
        star.move()
    root.after(10, main)

#========================

root = tkinter.Tk()
root.title('Space')
root.geometry('600x400')
canvas = tkinter.Canvas(root, width=600, height=400, bg='black')
canvas.pack()

stars = []
for i in range(100):
    c = Circle()  # インスタンスを生成
    c.draw()  # 定義したインスタンスメソッドを呼び出し
    stars.append(c)

main()
root.mainloop()
