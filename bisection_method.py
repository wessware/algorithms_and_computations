def math_bisection(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        exit(0)

    c = a
    while (b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c