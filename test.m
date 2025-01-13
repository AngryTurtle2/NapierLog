% 定义符号变量
clc
clear all

syms t x(t) r L
% 定义微分方程
ode = diff(x,t) == log(1 - r) * x;
% 求解微分方程，给定初始条件 
cond = x(0) == L;
xSol(t) = dsolve(ode, cond);
% 输出结果
disp(xSol(t)); 

%%
clc
clear all

syms t x(t) r L
% 定义函数表达式
x(t) = L*(1-r)^t;
% 对函数f(x)求导
dx_dt = diff(x,t);
% 输出结果
disp(dx_dt); 