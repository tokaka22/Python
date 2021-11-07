import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

'''
Solution
Include zero in the domain array, and suppress the divide by zero. This forces one element of the returned co-domain array as "inf", and "inf" is not plotted.
https://stackoverflow.com/questions/44041021/how-to-plot-y-1-x-as-a-single-graph
'''
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return 1/x
fx_name = r'$f(x)=\frac{1}{x}$'

# using 10XXX01 steps results in in array including the value 0
x=np.linspace(-100,100,10001)
# f(0) = nan -> a nan value creates a gap

# f = lambda t: (-0.0087697 + (1/4)*np.exp(-2/t)/(np.pi*t*((1/4)/(np.pi*t) + np.exp(-1/t)/(np.pi*t) + np.exp(-2/t)/(np.pi*t) + np.exp(-4/t)/(np.pi*t) + 2*np.exp(-5/t)/(np.pi*t) + np.exp(-8/t)/(np.pi*t) + np.exp(-9/t)/(np.pi*t) + 2*np.exp(-10/t)/(np.pi*t) + 2*np.exp(-13/t)/(np.pi*t) + np.exp(-18/t)/(np.pi*t) + np.exp(-1/2/t)/(np.pi*t) + 2*np.exp(-5/2/t)/(np.pi*t) + np.exp(-9/2/t)/(np.pi*t) + 2*np.exp(-13/2/t)/(np.pi*t) + 2*np.exp(-17/2/t)/(np.pi*t) + 3*np.exp(-25/2/t)/(np.pi*t) + 2*np.exp(-29/2/t)/(np.pi*t) + 2*np.exp(-37/2/t)/(np.pi*t) + np.exp(-49/2/t)/(np.pi*t) + np.exp(-1/4/t)/(np.pi*t) + 2*np.exp(-5/4/t)/(np.pi*t) + np.exp(-9/4/t)/(np.pi*t) + 2*np.exp(-13/4/t)/(np.pi*t) + 2*np.exp(-17/4/t)/(np.pi*t) + 3*np.exp(-25/4/t)/(np.pi*t) + 2*np.exp(-29/4/t)/(np.pi*t) + 2*np.exp(-37/4/t)/(np.pi*t) + 2*np.exp(-41/4/t)/(np.pi*t) + 2*np.exp(-45/4/t)/(np.pi*t) + np.exp(-49/4/t)/(np.pi*t) + 2*np.exp(-53/4/t)/(np.pi*t) + 2*np.exp(-61/4/t)/(np.pi*t) + 2*np.exp(-65/4/t)/(np.pi*t) + 2*np.exp(-85/4/t)/(np.pi*t))))

# f = lambda t: (-0.1104 + 24873.049744046*np.exp(-1243.6524872023/t)/(np.pi*t*(248.73049744046/(np.pi*t) + 994.921989761839*np.exp(-1989.84397952368/t)/(np.pi*t) + 1989.84397952368*np.exp(-1243.6524872023/t)/(np.pi*t) + 994.921989761839*np.exp(-994.921989761839/t)/(np.pi*t) + 994.921989761839*np.exp(-497.460994880919/t)/(np.pi*t) + 994.921989761839*np.exp(-248.73049744046/t)/(np.pi*t))))

# t = 80
# f = lambda t: (-0.0018382 + 2.5*np.exp(-145.0/t)/(np.pi*t*(2.5/(np.pi*t) + 10.0*np.exp(-245.0/t)/(np.pi*t) + 20.0*np.exp(-212.5/t)/(np.pi*t) + 20.0*np.exp(-185.0/t)/(np.pi*t) + 10.0*np.exp(-180.0/t)/(np.pi*t) + 20.0*np.exp(-162.5/t)/(np.pi*t) + 20.0*np.exp(-152.5/t)/(np.pi*t) + 20.0*np.exp(-145.0/t)/(np.pi*t) + 20.0*np.exp(-132.5/t)/(np.pi*t) + 20.0*np.exp(-130.0/t)/(np.pi*t) + 30.0*np.exp(-125.0/t)/(np.pi*t) + 10.0*np.exp(-122.5/t)/(np.pi*t) + 20.0*np.exp(-112.5/t)/(np.pi*t) + 20.0*np.exp(-102.5/t)/(np.pi*t) + 20.0*np.exp(-100.0/t)/(np.pi*t) + 20.0*np.exp(-92.5/t)/(np.pi*t) + 10.0*np.exp(-90.0/t)/(np.pi*t) + 20.0*np.exp(-85.0/t)/(np.pi*t) + 10.0*np.exp(-80.0/t)/(np.pi*t) + 20.0*np.exp(-72.5/t)/(np.pi*t) + 20.0*np.exp(-65.0/t)/(np.pi*t) + 30.0*np.exp(-62.5/t)/(np.pi*t) + 20.0*np.exp(-50.0/t)/(np.pi*t) + 10.0*np.exp(-45.0/t)/(np.pi*t) + 20.0*np.exp(-42.5/t)/(np.pi*t) + 10.0*np.exp(-40.0/t)/(np.pi*t) + 20.0*np.exp(-32.5/t)/(np.pi*t) + 20.0*np.exp(-25.0/t)/(np.pi*t) + 10.0*np.exp(-22.5/t)/(np.pi*t) + 10.0*np.exp(-20.0/t)/(np.pi*t) + 20.0*np.exp(-12.5/t)/(np.pi*t) + 10.0*np.exp(-10.0/t)/(np.pi*t) + 10.0*np.exp(-5.0/t)/(np.pi*t) + 10.0*np.exp(-2.5/t)/(np.pi*t))))

f = lambda t: (6.01159923143594*np.exp(-48.0927938514875/t)/(np.pi*t*(6.01159923143594/(np.pi*t) + 24.0463969257437*np.exp(-48.0927938514875/t)/(np.pi*t) + 48.0927938514875*np.exp(-30.0579961571797/t)/(np.pi*t) + 24.0463969257437*np.exp(-24.0463969257437/t)/(np.pi*t) + 24.0463969257437*np.exp(-12.0231984628719/t)/(np.pi*t) + 24.0463969257437*np.exp(-6.01159923143594/t)/(np.pi*t))) + 18.0347976943078*np.exp(-30.0579961571797/t)/(np.pi*t*(6.01159923143594/(np.pi*t) + 24.0463969257437*np.exp(-48.0927938514875/t)/(np.pi*t) + 48.0927938514875*np.exp(-30.0579961571797/t)/(np.pi*t) + 24.0463969257437*np.exp(-24.0463969257437/t)/(np.pi*t) + 24.0463969257437*np.exp(-12.0231984628719/t)/(np.pi*t) + 24.0463969257437*np.exp(-6.01159923143594/t)/(np.pi*t))) + 6.01159923143594*np.exp(-24.0463969257437/t)/(np.pi*t*(6.01159923143594/(np.pi*t) + 24.0463969257437*np.exp(-48.0927938514875/t)/(np.pi*t) + 48.0927938514875*np.exp(-30.0579961571797/t)/(np.pi*t) + 24.0463969257437*np.exp(-24.0463969257437/t)/(np.pi*t) + 24.0463969257437*np.exp(-12.0231984628719/t)/(np.pi*t) + 24.0463969257437*np.exp(-6.01159923143594/t)/(np.pi*t))) + 6.01159923143594*np.exp(-12.0231984628719/t)/(np.pi*t*(6.01159923143594/(np.pi*t) + 24.0463969257437*np.exp(-48.0927938514875/t)/(np.pi*t) + 48.0927938514875*np.exp(-30.0579961571797/t)/(np.pi*t) + 24.0463969257437*np.exp(-24.0463969257437/t)/(np.pi*t) + 24.0463969257437*np.exp(-12.0231984628719/t)/(np.pi*t) + 24.0463969257437*np.exp(-6.01159923143594/t)/(np.pi*t))) + 6.01159923143594*np.exp(-6.01159923143594/t)/(np.pi*t*(6.01159923143594/(np.pi*t) + 24.0463969257437*np.exp(-48.0927938514875/t)/(np.pi*t) + 48.0927938514875*np.exp(-30.0579961571797/t)/(np.pi*t) + 24.0463969257437*np.exp(-24.0463969257437/t)/(np.pi*t) + 24.0463969257437*np.exp(-12.0231984628719/t)/(np.pi*t) + 24.0463969257437*np.exp(-6.01159923143594/t)/(np.pi*t))))

y=f(x)
# print(x.shape)
# print(y.shape)
# print(x)
# print(y)
res = fsolve(f, 2)
print(50*"=")
print(res)
print(f(res))

plt.plot(x, y)
y1 = 0*x
plt.plot(x, y1, 'r')
# plt.xticks(range(-5, 5))
# plt.yticks(range(-5, 5))
plt.legend(loc='upper left')
plt.show()


'''
写得像坨shi
'''
# t = np.arange(-5.0, 5.0, 0.1)
# # t1 = np.arange(-100.0, -0.000001, 0.1)
# # t2 = np.arange(0.000001, 100.0, 0.1)
# # t = np.concatenate((t1, t2))
# # t = np.arange(-100.0, 0.0, 0.1)
# # print(t1)
# # print(t2)
# # print(t)

# # # the function, which is y = x^2 here
# # f = lambda t: (-0.0087697 + (1/4)*np.exp(-2/t)/(np.pi*t*((1/4)/(np.pi*t) + np.exp(-1/t)/(np.pi*t) + np.exp(-2/t)/(np.pi*t) + np.exp(-4/t)/(np.pi*t) + 2*np.exp(-5/t)/(np.pi*t) + np.exp(-8/t)/(np.pi*t) + np.exp(-9/t)/(np.pi*t) + 2*np.exp(-10/t)/(np.pi*t) + 2*np.exp(-13/t)/(np.pi*t) + np.exp(-18/t)/(np.pi*t) + np.exp(-1/2/t)/(np.pi*t) + 2*np.exp(-5/2/t)/(np.pi*t) + np.exp(-9/2/t)/(np.pi*t) + 2*np.exp(-13/2/t)/(np.pi*t) + 2*np.exp(-17/2/t)/(np.pi*t) + 3*np.exp(-25/2/t)/(np.pi*t) + 2*np.exp(-29/2/t)/(np.pi*t) + 2*np.exp(-37/2/t)/(np.pi*t) + np.exp(-49/2/t)/(np.pi*t) + np.exp(-1/4/t)/(np.pi*t) + 2*np.exp(-5/4/t)/(np.pi*t) + np.exp(-9/4/t)/(np.pi*t) + 2*np.exp(-13/4/t)/(np.pi*t) + 2*np.exp(-17/4/t)/(np.pi*t) + 3*np.exp(-25/4/t)/(np.pi*t) + 2*np.exp(-29/4/t)/(np.pi*t) + 2*np.exp(-37/4/t)/(np.pi*t) + 2*np.exp(-41/4/t)/(np.pi*t) + 2*np.exp(-45/4/t)/(np.pi*t) + np.exp(-49/4/t)/(np.pi*t) + 2*np.exp(-53/4/t)/(np.pi*t) + 2*np.exp(-61/4/t)/(np.pi*t) + 2*np.exp(-65/4/t)/(np.pi*t) + 2*np.exp(-85/4/t)/(np.pi*t))))
# # # f = lambda t: -0.0283650420606136 + 0.00998884001938087*np.exp(-0.0399553600775235/t)
# # y1 = f(t1)
# # y2 = f(t2)
# # # y1 = 1/t1
# # # y2 = 1/t2
# # # y = x**2

# # # plot the function
# # plt.plot(t1,y1, 'r')
# # plt.plot(t2,y2, 'r')
# # y = 0*t


# ### test 1/t
# y = 1/t
# print(y.shape)
# print(t.shape)
# plt.plot(t,y,'b')
# # show the plot
# plt.show()

# # res = fsolve(f, 75)
# # print(res)
# # print(f(0.000001))