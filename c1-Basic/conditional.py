def main():
    x,y = 10000,1000
    if x < y:
        result = "x is less than y"
    elif x == y:
        result  = "x is the same as a y"
    else:
        result = "x is greater than y"

    print(result)

    #condtional statements let you use "a if c else b"
    result = "x is less than y" if x<y else ("x is greater or equal to y")
    print(result)

    #match-case makes it easy to compare multiple values
    # value = "one"
    # match value:
    #     case "one":
    #         result = 1
    #     case "two":
    #         result = 2
    #     case "three" | "four":
    #         result = (3,4)
    #     case _:
    #         result = -1
    # print(result)   ------> only possible in python 3.10


if __name__ == "__main__":
    main()