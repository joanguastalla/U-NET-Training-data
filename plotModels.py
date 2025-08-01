import numpy as np
import matplotlib.pyplot as plt
import os 



## ZO parameters
ns=876
nm=134
nt=864

m0=1        
mf=4.6
dmtick=0.6
dm=0.03
dticks=int(dmtick/dm)
midticks=np.arange(0,120+dticks,dticks)
mid=np.round(np.arange(m0,mf+dmtick,dmtick),decimals=1)

dttick=0.5
dt=0.004
tf=3.0
dtick=int(dttick/dt)

timeticks=np.arange(0,int(tf/dt) + dtick,dtick)
times=np.arange(0,tf + dttick,dttick)


## Velocity model parameters
nz=335
nx=600

zf=3
xf=5.5
dzratio=0.5
dx=dz=0.01
dzr=int(dzratio/dz)
xposticks=np.arange(0,int(xf/dx)+ dzr,dzr)
xpos=np.arange(0,xf+dzratio,dzratio)

zdepsticks=np.arange(0,int(zf/dz) + dzr,dzr)
zdeps=np.arange(0,zf + dzratio,dzratio)



Lines=["XLine","YLine"]
linebeg=0
lineend=280
dline=4
pad=20


for line in Lines:
    for i in range(linebeg,lineend+dline,dline):
        basedir=f"Dataset/{line}{i}"
        velfile=f"{basedir}/vp.bin"
        zofile= f"{basedir}/zo.bin"
        zostackfile=f"{basedir}/zostack.bin"
        maskfile=f"{basedir}/zomask.bin"
        if not os.path.exists(basedir):
            continue

        fig, axes = plt.subplots(2, 2, figsize=(18, 10))
        pad = 20

        V=np.fromfile(velfile,dtype=np.float32).reshape((nx,nz)).T
        ZO=np.fromfile(zofile,dtype=np.float32).reshape((nm,ns)).T
        ZOAGC=np.fromfile(zostackfile,dtype=np.float32).reshape((nm,ns)).T
        M=np.fromfile(maskfile,dtype=np.float32).reshape((nm,ns)).T
        ZO[:100,:]=0.0                  # cut direct wave

        # Velocity Model
        im = axes[0, 0].imshow(V, aspect="equal", cmap="seismic")
        axes[0, 0].set_title(f"Modelo de velocidade ({line}{i})", pad=pad)
        axes[0, 0].set_xticks(xposticks)
        axes[0, 0].set_xticklabels(xpos)
        axes[0, 0].set_yticks(zdepsticks)
        axes[0, 0].set_yticklabels(zdeps)
        axes[0, 0].set_xlabel("Distância [km]")
        axes[0, 0].set_ylabel("Profundidade [km]", rotation=-90, labelpad=20)
        axes[0, 0].xaxis.set_label_position('top')
        axes[0, 0].xaxis.set_ticks_position('top')
        cbar = fig.colorbar(im, ax=axes[0, 0])
        cbar.set_label("Velocidade [km/s]")

        # ZO Section
        im = axes[0, 1].imshow(ZO, aspect="auto", cmap="gray_r")
        axes[0, 1].set_title(f"Seção ZO ({line}{i})", pad=pad)
        axes[0, 1].set_xticks(midticks)
        axes[0, 1].set_xticklabels(mid)
        axes[0, 1].set_yticks(timeticks)
        axes[0, 1].set_yticklabels(times)
        axes[0, 1].set_xlabel("Ponto médio [km]")
        axes[0, 1].set_ylabel("Tempo [s]", rotation=-90, labelpad=20)
        axes[0, 1].xaxis.set_label_position('top')
        axes[0, 1].xaxis.set_ticks_position('top')
        cbar = fig.colorbar(im, ax=axes[0, 1])
        cbar.set_label("Amplitude [Pa]")

        # Simulated ZO
        im = axes[1, 0].imshow(ZOAGC, aspect="auto", cmap="gray_r")
        axes[1, 0].set_title(f"Seção ZO simulada ({line}{i})", pad=pad)
        axes[1, 0].set_xticks(midticks)
        axes[1, 0].set_xticklabels(mid)
        axes[1, 0].set_yticks(timeticks)
        axes[1, 0].set_yticklabels(times)
        axes[1, 0].set_xlabel("Ponto médio [km]")
        axes[1, 0].set_ylabel("Tempo [s]", rotation=-90, labelpad=20)
        axes[1, 0].xaxis.set_label_position('top')
        axes[1, 0].xaxis.set_ticks_position('top')
        cbar = fig.colorbar(im, ax=axes[1, 0])
        cbar.set_label("Amplitude [Pa]")

        # ZO Mask
        im = axes[1, 1].imshow(M, aspect="auto", cmap="gray_r")
        axes[1, 1].set_title(f"Máscara de tempos de trânsito ({line}{i})", pad=pad)
        axes[1, 1].set_xticks(midticks)
        axes[1, 1].set_xticklabels(mid)
        axes[1, 1].set_yticks(timeticks)
        axes[1, 1].set_yticklabels(times)
        axes[1, 1].set_xlabel("Ponto médio [km]")
        axes[1, 1].set_ylabel("Tempo [s]", rotation=-90, labelpad=20)
        axes[1, 1].xaxis.set_label_position('top')
        axes[1, 1].xaxis.set_ticks_position('top')
        cbar = fig.colorbar(im, ax=axes[1, 1])
        cbar.set_ticks([0,1])
        cbar.set_label("Máscara")

        plt.tight_layout()
        plt.show()



