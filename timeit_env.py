import timeit


if __name__ == "__main__":

    # REPLACE CODE BELOW WITH CODE YOU WANT TO TEST <----------------------------------------------------------- (1)


    # ADD CODE BLOCK ABOVE HERE  -------------------------------------------------------------------------------

if __name__ == "__main__":
    # EDIT THE FOLLOWING LINES TO SPECIFY THE FUNCTION, ITS ARGS, AND THE NUMBER OF TESTS YOU WANT TO RUN <----- (2)
    loop = 1000000
    result = timeit.timeit('decode()', globals=globals(), number=loop)
    print(result / loop)
