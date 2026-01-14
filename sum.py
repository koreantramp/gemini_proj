def main():
    try:
        # 사용자로부터 두 숫자 입력 받기
        num1_str = input("첫 번째 숫자를 입력하세요: ")
        num2_str = input("두 번째 숫자를 입력하세요: ")

        # 입력값을 실수형으로 변환
        num1 = float(num1_str)
        num2 = float(num2_str)

        # 합계 계산
        total = num1 + num2

        # 결과 출력 (정수일 경우 정수로 출력, 아니면 실수로 출력)
        if total.is_integer():
            print(f"두 숫자의 합: {int(total)}")
        else:
            print(f"두 숫자의 합: {total}")

    except ValueError:
        print("오류: 유효한 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
