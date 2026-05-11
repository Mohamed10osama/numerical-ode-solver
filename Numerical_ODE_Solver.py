import numpy as np
import matplotlib.pyplot as plt
print("===This project aims to solve differential equation dy/dx=-y using euler method and Runge Kutta method ===")
x_values=np.linspace(0,5,51) #divide x intervals
y_eulervalues=np.zeros(51) #make y values all zeros at first
y_rkvalues=np.zeros(51) #make y values all zeros at first
y_eulervalues[0]=1    #initial value : y(0)=1 
y_rkvalues[0]=1 #initial value : y(0)=1 
h=0.1 #step value
y_exact=np.exp(-x_values) #exact solution
# ===== Euler method =====
for i in range (50): #loop for euler numerical solution
    y_eulervalues[i+1]=y_eulervalues[i]-y_eulervalues[i]*h
plt.figure(figsize=(7,7)) 
plt.plot(x_values,y_eulervalues,"bo--",label="Euler method",linewidth=3) #numerical solution in blue line
plt.plot(x_values,y_exact,"r-",label="Exact Solution",linewidth=3) #numerical solution in red line
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Solving differntial equation with Euler method")
plt.legend() #making a label indicator
plt.grid(True)
plt.savefig('Eulermethod.png', dpi=150)
plt.show()
print("===Euler method results===")
print(f"MAX error is {np.abs(y_eulervalues-y_exact).max():.4f}")
print(f"Final numerical value is{y_eulervalues[-1]:.4f}")
print(f"Final exact value is{y_exact[-1]:.4f}")
# ===== Runge Kutta method =====
for i in range (50): #loop for Runge Kutta numerical solution 
    k1=-y_rkvalues[i]
    k2=-(y_rkvalues[i]+0.5*h*k1)
    k3=-(y_rkvalues[i]+0.5*h*k2)
    k4=-(y_rkvalues[i]+h*k3)
    y_rkvalues[i+1]=y_rkvalues[i]+h*(k1+2*k2+2*k3+k4)/6
plt.figure(figsize=(7,7)) 
plt.plot(x_values,y_rkvalues,"bo--",label="RK4 method",linewidth=3) #numerical solution in blue line
plt.plot(x_values,y_exact,"r-",label="Exact Solution",linewidth=3) #numerical solution in red line
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Solving differntial equation with RK4")
plt.legend() #making a label indicator
plt.grid(True)
plt.savefig('RK4.png', dpi=150)
plt.show()
print("===Runge Kutta4 results===")
print(f"MAX error is{np.abs(y_rkvalues-y_exact).max():.4f}")
print(f"Final numerical value is{y_rkvalues[-1]:.4f}")
print(f"Final exact value is{y_exact[-1]:.4f}")
# ===== Comparison Plot =====
plt.figure(figsize=(9, 6))
plt.plot(x_values, y_eulervalues, "bo--", label="Euler Method", linewidth=2)
plt.plot(x_values, y_rkvalues,    "gs--", label="RK4 Method",   linewidth=2)
plt.plot(x_values, y_exact,       "r-",   label="Exact Solution: e^(-x)", linewidth=2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Euler vs RK4 — Solving dy/dx = -y")
plt.legend()
plt.grid(True)
plt.savefig('comparison.png', dpi=150)
plt.show()

# ===== Error Comparison Plot =====
euler_error = np.abs(y_eulervalues - y_exact)
rk4_error   = np.abs(y_rkvalues - y_exact)

plt.figure(figsize=(9, 5))
plt.plot(x_values, euler_error, "b-", label="Euler Error", linewidth=2)
plt.plot(x_values, rk4_error,   "g-", label="RK4 Error",   linewidth=2)
plt.xlabel("X")
plt.ylabel("Absolute Error")
plt.title("Error Comparison: Euler vs RK4")
plt.legend()
plt.grid(True)
plt.savefig('error_comparison.png', dpi=150)
plt.show()