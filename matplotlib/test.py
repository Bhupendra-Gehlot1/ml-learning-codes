import matplotlib.pyplot as plt
import numpy as np;

x = np.linspace(0,10,100);
y = np.sin(x);
z = np.cos(x);

# plt.plot(x,y);
# plt.show()

# plt.plot(x,z);
# plt.xlabel('angle value')
# plt.ylabel('cosine value')
# plt.title('Cosine Graph')
# plt.show()


# x=np.linspace(-10,10,20);
# y= x**2;
# plt.plot(x,y)
# plt.show()

# plt.plot(x,y,'r+')
# plt.show()


# fig=plt.figure();
# ax= fig.add_axes([0,0,1,1])
# Lan= ["Eng","Hindi","Urdu","French","Tamil"]
# ppls = [100,120,150,20,102]
# # ax.bar(Lan,ppls)
# ax.pie(ppls,labels=Lan,autopct="%1.1f%%")
# ax.scatter(x,y,color="r")
# ax.scatter(x,z,color="g")
# plt.xlabel("Lan")
# plt.ylabel("ppls")
# plt.title("bar chart")
# plt.show()


fig = plt.figure();
ax = plt.axes(projection='3d')
ax.scatter(x,y,z,c=z,cmap="Reds")
plt.show()