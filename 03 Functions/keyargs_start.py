# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(x, y, *, SurpressErros=False):
    pass


def main():
    # try to call the function without the keyword
    myFunction(1, 2, SurpressErros=True)


if __name__ == "__main__":
    main()
