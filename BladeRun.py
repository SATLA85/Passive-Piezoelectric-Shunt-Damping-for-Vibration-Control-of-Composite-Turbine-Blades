import subprocess
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

PL = [0, 1]

## Start The FEM iteration analysis

for k in range(len(PL)):
    file1 = open("Iter_param_Frequ.inp", "w+")
    file1.write('shunt=%e\n' % PL[k])
    file1.close()
    cmd = ["C:\Program Files\ANSYS Inc\\v201\\ansys\\bin\winx64\ANSYS201.exe", '-b', '-p', 'ANSYS', '-i',
           'D:\Berlin_Conf\Blade_Sunt.txt.txt', '-o',
           'D:\Berlin_Conf\\Blade_out.txt']
    subprocess.call(cmd)

Lables=['Without Control','With Control']
cl=['dashed','solid']
cll=['r','k']
MRK=[None,'o']
plt.rcParams['font.size'] = 20
for k in range(len(PL)):
    Y = np.loadtxt(str(k)+'results_Harmonic.txt', delimiter=',')
    plt.plot(np.arange(1,151,1, dtype=int), np.abs(Y[:,1]), label=Lables[k], color=cll[k], linestyle=cl[k], marker=MRK[k])
    plt.legend()
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Amplitude (dB)')
    #plt.xlim([80,150])
    plt.xlim([250, 300])


Lables=['Without Control','With Control']
cl=['dashed','solid']
cll=['r','k']
MRK=[None,'o']
plt.rcParams['font.size'] = 20
for k in range(len(PL)):
    Y = np.loadtxt(str(k)+'SENSACTBlade.txt', delimiter=',')
    plt.plot(Y[:,0], Y[:,3], label=Lables[k], color=cll[k], linestyle=cl[k], marker=MRK[k])
    plt.legend()
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (mm)')
    #plt.xlim([80,150])
    plt.xlim([250, 300])

