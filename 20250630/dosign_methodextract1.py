class Node:
    def __init__(self, date_code, name):
        self.date_code = date_code
        self.name = name
        self.is_signed = False

    def do_sign(self):
        self.is_signed = True

    def print_sign(self):
        print(f"{self.date_code} : {self.name}")


class SignManager:
    def __init__(self, signs):
        self.signs : list[Node] = signs

    # 1. 서명 정렬하기
    def sort_by_date(self):
        for y in range(len(self.signs)):
            for x in range(y + 1, len(self.signs)):
                if self.signs[y].date_code > self.signs[x].date_code:
                    self.signs[y], self.signs[x] = self.signs[x], self.signs[y]

    # 2. valid 검사
    def validate_date(self):
        flag = True
        for tar in self.signs:
            if 0 < tar.date_code < 10:
                continue
            flag = False
            break
        return flag

    # 3. 서명 하기
    def sign_all(self):
        for tar in self.signs:
            tar.do_sign()
            tar.print_sign()

    def run(self):
        self.sort_by_date()
        if self.validate_date():
            self.sign_all()
        else:
            raise Exception()

if __name__ == "__main__":
    arr = list()
    arr.append(Node(5, "KFC"))
    arr.append(Node(1, "JASON"))
    arr.append(Node(2, "LUCKY"))
    sign = SignManager(arr)

    try:
        sign.run()
    except Exception:
        pass