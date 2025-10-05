# factorial.py
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

if __name__ == "__main__":
    try:
        num = int(input("একটি পূর্ণসংখ্যা দিন (>=0): ").strip())
        if num < 0:
            print("ত্রুটি: নেগেটিভ সংখ্যা নেই। দয়া করে 0 বা ধনাত্মক সংখ্যা দিন।")
        else:
            print(f"{num} এর factorial = {factorial(num)}")
    except ValueError:
        print("ত্রুটি: অনুগ্রহ করে একটি বৈধ পূর্ণসংখ্যা দিন।")
