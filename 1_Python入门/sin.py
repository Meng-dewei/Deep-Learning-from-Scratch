# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# ��������
x = np.arange(0, 6, 0.1) # ��0.1Ϊ��λ������0��6������
y = np.sin(x)

# ����ͼ��
plt.plot(x,y)
plt.show()