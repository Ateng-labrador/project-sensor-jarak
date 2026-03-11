import pandas as pd

def conver_cvs(a, b):
    """
    a = nama file cvs
    b = nama variabel
    """
    with open(a, "w") as file_csv:
        file_csv.write(b)

def add_time(b, jalur, filename):
    """
    b = data series (panjang data)
    jalur = dataframe
    filename = nama file untuk disimpan
    """
    time = []
    for i in range(1, len(b) + 1):
        time.append(str(i))
    time_list = time
    jalur['waktu'] = time_list
    jalur.to_csv(filename, index=False)


# Putaran Pertama

data_1_6_naik = """
jarak
6.21
6.21
6.21
6.21
6.11
6.11
6.21
6.21
6.21
6.21
""" 

data_1_9_naik = """
jarak
9.18
9.42
9.40
9.50
9.40
9.40
9.52
9.40
9.40
9.52
"""

data_1_12_naik = """
jarak
12.25
12.14
12.23
12.13
12.23
12.13
12.13
13.48
12.14
12.23
12.14
"""

data_1_15_naik = """
jarak
15.19
15.19
15.19
15.19
15.19
15.19
15.19
15.19
15.19
15.19
"""

data_1_18_naik = """
jarak
17.78
17.78
17.78
17.78
17.77
17.78
17.78
17.78
17.78
17.77
"""

data_1_21_naik = """
jarak
21.28
21.28
21.30
20.34
21.20
21.18
21.20
21.20
21.28
21.30
"""

data_1_24_naik = """
jarak
24.28
24.27
23.39
23.41
23.29
23.29
23.39
23.39
23.41
23.41
"""

data_1_27_naik = """
jarak
27.17
27.06
27.17
27.06
27.17
27.06
27.06
27.06
27.17
27.06
27.06
27.17
27.17
27.06
27.06
27.17
27.06
27.06
27.06
"""

data_1_30_naik = """
jarak
29.17
29.15
29.05
29.17
29.05
29.15
29.07
29.17
29.05
29.15
"""

data_1_27_turun = """
jarak
27.17
27.37
27.94
27.06
26.21
26.31
26.21
26.29
26.31
26.21
"""

data_1_24_turun = """
jarak
24.75
24.18
24.16
24.16
24.27
24.27
24.27
24.16
24.27
24.27
24.16
24.28
24.28
24.28
24.16
24.16
24.27
24.27
24.25
24.16
24.28
24.27
24.27
24.16
24.16
24.27
24.27
24.16
24.28
24.27
"""

data_1_21_turun = """
jarak
21.30
21.18
20.97
20.97
20.97
20.97
20.97
20.97
20.97
20.97
20.97
20.96
20.97
21.93
"""

data_1_18_turun = """
jarak
18.73
18.11
18.42
18.42
18.73
18.74
18.74
18.64
18.73
18.74
18.74
18.74
18.74
18.73
18.73
18.73
18.74
18.74
18.74
18.73
18.74
18.73
18.74
18.73
18.74
18.64
18.73
18.74
18.74
18.73
18.73
18.74
18.74
18.73
18.73
18.74
18.62
18.74
18.74
18.74
18.73
18.73
18.73
18.73
18.73
18.73
18.69
18.74
18.73
"""

data_1_15_turun = """
jarak
15.86
15.54
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.86
15.86
15.86
15.86
"""

data_1_12_turun = """
jarak
12.91
12.81
12.57
12.13
12.23
12.13
12.13
12.14
12.13
12.13
12.13
12.13
12.14
12.23
12.13
12.23
12.13
12.25
12.14
12.23
12.14
12.25
12.13
12.13
12.13
12.13
12.14
12.13
12.13
12.13
12.23
12.13
12.23
12.13
12.23
12.13
12.23
12.13
12.13
12.13
12.13
12.13
12.13
12.13
12.13
12.25
12.13
12.25
12.13
12.23
12.13
12.23
12.13
12.23
12.13
12.13
12.13
12.13
12.13
12.13
12.13
12.13
"""

data_1_9_turun = """
jarak
9.74
9.18
9.07
9.07
9.18
9.18
9.07
9.16
9.18
9.06
9.07
9.18
9.06
9.07
9.18
9.06
9.07
9.18
9.18
9.06
9.18
9.16
9.07
9.16
9.18
9.07
9.07
9.18
9.06
9.07
9.18
9.07
9.06
9.18
9.18
9.06
9.18
9.16
9.06
9.07
9.16
9.07
9.07
9.18
9.06
9.07
9.18
9.18
9.07
9.18
9.18
9.07
9.18
9.18
9.07
9.07
9.18
9.06
9.07
"""

data_1_6_turun = """
jarak
6.53
6.21
6.21
6.21
6.84
6.86
6.84
6.76
6.86
6.76
6.86
6.74
6.76
6.84
6.86
6.86
6.86
6.74
6.76
6.86
6.84
6.86
6.76
6.76
6.86
6.86
6.86
6.86
6.76
6.76
6.86
6.86
6.84
6.76
6.86
6.74
6.74
6.86
6.86
6.86
6.74
6.76
6.76
6.86
6.84
6.86
6.74
"""

# Putaran Kedua

data_2_6_naik = """
jarak
6.53
5.23
5.23
5.23
5.23
5.56
5.45
5.45
5.45
5.56
"""
data_2_9_naik = """
jarak
9.76
8.83
8.83
8.83
8.83
8.83
8.83
8.83
8.83
8.83
8.83
"""
data_2_12_naik = """
jarak
12.23
12.23
12.13
12.13
12.14
12.13
12.13
12.13
12.23
12.14
12.23
12.14
12.23
12.14
12.23
12.13
12.25
12.13
12.13
12.13
12.14
12.13
12.13
12.14
12.13
12.23
12.13
12.23
12.13
12.23
12.13
"""
data_2_15_naik = """
jarak
15.54
15.86
15.86
15.86
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.56
"""
data_2_18_naik = """
jarak
18.42
18.09
17.13
17.17
17.13
17.15
17.15
17.13
17.15
17.13
"""
data_2_21_naik = """
jarak
20.01
21.51
20.01
20.01
20.01
20.01
20.01
20.01
20.01
20.01
"""
data_2_24_naik = """
jarak
23.41
23.41
23.31
23.31
24.28
22.54
22.54
22.54
22.54
22.54
"""
data_2_27_naik = """
jarak
26.60
26.77
26.02
26.60
26.87
26.21
26.48
26.48
27.06
27.92
"""
data_2_30_naik = """
jarak
29.15
28.21
28.23
28.21
28.21
28.33
28.21
28.31
28.23
28.31
"""

data_2_6_turun = """
jarak
6.11
5.45
5.13
5.23
5.23
5.25
5.23
5.23
5.25
5.25
"""
data_2_9_turun = """
jarak
9.40
9.84
9.74
9.76
9.86
9.74
9.74
9.84
9.74
9.74
9.84
9.74
9.74
9.84
9.74
9.84
9.84
9.74
8.83
9.84
9.74
9.84
9.84
9.74
9.86
9.74
9.74
9.84
9.74
9.74
9.86
9.74
9.74
9.86
8.37
9.76
9.84
9.74
9.76
8.47
8.37
8.35
8.45
8.47
9.74
9.78
8.47
9.74
9.74
9.84
9.76
"""
data_2_12_turun = """
jarak
12.91
12.25
12.13
15.19
15.19
15.19
15.30
15.21
15.19
15.30
"""
data_2_15_turun = """
jarak
15.86
15.86
15.54
15.56
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.19
15.86
"""
data_2_18_turun = """
jarak
18.73
18.09
18.42
17.13
17.13
17.13
17.15
17.15
17.13
17.15
17.13
17.15
17.13
17.13
17.15
"""
data_2_21_turun = """
jarak
21.61
22.83
22.54
22.43
22.43
22.43
22.54
22.54
22.54
22.54
"""
data_2_24_turun = """
jarak
24.75
23.98
25.43
25.42
25.33
25.43
25.42
25.33
25.33
25.90
25.90
"""
data_2_27_turun = """
jarak
27.06
27.17
27.94
27.92
27.94
27.94
27.94
27.92
27.94
27.94
27.92
27.94
27.94
27.94
27.94
27.94
27.94
27.92
27.94
"""
data_2_30_turun = """
jarak
29.15
28.21
28.23
28.21
28.21
28.33
28.21
28.31
28.23
28.31
"""

# Putaran Ketiga

data_3_6_naik = """
jarak
6.53
6.53
6.43
6.43
5.56
5.56
5.56
5.57
5.56
6.53
"""
data_3_9_naik = """
jarak
9.74
9.18
9.16
9.06
9.16
9.18
9.07
9.07
9.18
9.06
9.07
9.16
9.07
9.07
9.16
9.16
9.07
9.18
9.18
9.06
9.18
9.18
9.06
9.07
9.18
9.07
9.07
9.18
9.06
9.06
9.16
9.16
9.06
9.18
9.18
9.07
9.06
9.16
9.06
9.07
9.16
9.07
9.74
9.50
"""
data_3_12_naik = """
jarak
12.13
12.57
12.57
12.47
12.47
12.47
12.47
12.47
12.47
12.57
12.47
12.57
12.47
12.47
12.47
12.81
"""
data_3_15_naik = """
jarak
15.19
15.54
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.97
15.86
15.85
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.86
15.86
"""
data_3_18_naik = """
jarak
18.42
18.09
17.78
17.15
17.15
17.46
17.46
17.46
17.46
17.46
"""
data_3_21_naik = """
jarak
21.30
21.51
21.51
21.83
21.28
21.28
21.30
21.30
21.28
21.30
21.30
21.28
21.28
21.18
21.28
21.30
"""
data_3_24_naik = """
jarak
24.56
23.89
23.87
23.41
23.39
23.39
23.31
23.31
23.41
23.39
"""
data_3_27_naik = """
jarak
26.48
27.05
26.60
27.94
26.29
26.21
26.19
26.29
26.19
26.19
"""
data_3_30_naik = """
jarak
30.87
30.36
29.57
29.05
29.15
29.05
29.15
29.05
29.15
29.05
"""

data_3_6_turun = """
jarak
6.84
6.86
6.86
6.76
6.76
6.84
6.74
6.76
6.86
6.86
6.84
6.84
6.74
6.74
6.84
6.86
6.86
6.74
6.74
6.84
6.86
6.86
6.86
6.74
6.74
6.86
6.86
6.86
"""
data_3_9_turun = """
jarak
9.40
9.18
9.74
9.84
9.84
9.74
9.84
9.84
9.74
9.86
9.74
9.74
9.84
9.74
9.74
9.86
9.74
9.74
9.84
9.74
9.74
9.84
9.74
9.74
9.84
9.74
9.84
9.84
9.76
9.84
9.78
9.74
9.84
9.74
9.74
9.86
9.74
9.76
"""
data_3_12_turun = """
jarak
12.13
12.25
12.13
12.23
12.13
12.23
12.13
12.13
12.13
12.13
12.13
12.13
12.23
12.13
12.23
12.13
12.23
12.13
12.23
12.13
12.23
12.13
12.13
12.13
12.13
12.13
12.13
12.13
12.13
12.23
12.14
12.23
12.14
12.25
12.13
12.23
"""
data_3_15_turun = """
jarak
15.54
15.97
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.97
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.86
15.19
"""
data_3_18_turun = """
jarak
18.09
17.77
17.13
17.77
17.77
17.78
17.77
17.78
17.78
17.78
17.13
"""
data_3_21_turun = """
jarak
21.83
21.18
20.96
20.32
20.34
20.32
20.32
20.34
20.32
20.34
"""
data_3_24_turun = """
jarak
24.56
23.70
23.08
23.00
23.00
23.12
23.12
23.12
23.12
23.00
"""
data_3_27_turun = """
jarak
27.46
28.61
28.61
28.52
28.61
28.79
26.77
26.29
26.19
"""
data_3_30_turun = """
jarak
29.15
29.05
29.15
29.05
29.15
29.05
29.15
29.05
29.15
29.82
"""

# putaran pertama 


a1 = "data_1_6_naik.csv"
a2 = "data_1_9_naik.csv"
a3 = "data_1_12_naik.csv"
a4 = "data_1_15_naik.csv"
a5 = "data_1_18_naik.csv"
a6 = "data_1_21_naik.csv"
a7 = "data_1_24_naik.csv"
a8 = "data_1_27_naik.csv"
a9 = "data_1_30_naik.csv"


b1 = "data_1_6_turun.csv"
b2 = "data_1_9_turun.csv"
b3 = "data_1_12_turun.csv"
b4 = "data_1_15_turun.csv"
b5 = "data_1_18_turun.csv"
b6 = "data_1_21_turun.csv"
b7 = "data_1_24_turun.csv"
b8 = "data_1_27_turun.csv"
b9 = "data_1_30_turun.csv"

# putaran kedua

c1 = "data_2_6_naik.csv"
c2 =  "data_2_9_naik.csv"
c3 = "data_2_12_naik.csv"
c4 = "data_2_15_naik.csv"
c5 = "data_2_18_naik.csv"
c6 = "data_2_21_naik.csv"
c7 = "data_2_24_naik.csv"
c8 = "data_2_27_naik.csv"
c9 = "data_2_30_naik.csv"

d1 = "data_2_6_turun.csv"
d2 = "data_2_9_turun.csv"
d3 = "data_2_12_turun.csv"
d4 = "data_2_15_turun.csv"
d5 = "data_2_18_turun.csv"
d6 = "data_2_21_turun.csv"
d7 = "data_2_24_turun.csv"
d8 = "data_2_27_turun.csv"
d9 = "data_2_30_turun.csv"

# putaran ketiga

f1 = "data_3_6_naik.csv"
f2 = "data_3_9_naik.csv"
f3 = "data_3_12_naik.csv"
f4 = "data_3_15_naik.csv"
f5 = "data_3_18_naik.csv"
f6 = "data_3_21_naik.csv"
f7 = "data_3_24_naik.csv"
f8 = "data_3_27_naik.csv"
f9 = "data_3_30_naik.csv"

g1 = "data_3_6_turun.csv"
g2 = "data_3_9_turun.csv"
g3 = "data_3_12_turun.csv"
g4 = "data_3_15_turun.csv"
g5 = "data_3_18_turun.csv"
g6 = "data_3_21_turun.csv"
g7 = "data_3_24_turun.csv"
g8 = "data_3_27_turun.csv"
g9 = "data_3_30_turun.csv"


# putaran pertama
conver_cvs(a = a1, b = data_1_6_naik)
dt16up = pd.read_csv(a1)
x = dt16up['jarak']
add_time(x, dt16up, a1)

conver_cvs(a = a2, b = data_1_9_naik)
dt19up = pd.read_csv(a2)
x = dt19up['jarak']
add_time(x, dt19up, a2)

conver_cvs(a = a3, b = data_1_12_naik)
dt112up = pd.read_csv(a3)
x = dt112up['jarak']
add_time(x, dt112up, a3)

conver_cvs(a = a4, b = data_1_15_naik)
dt115up = pd.read_csv(a4)
x = dt115up['jarak']
add_time(x, dt115up, a4)

conver_cvs(a = a5, b = data_1_18_naik)
dt118up = pd.read_csv(a5)
x = dt118up['jarak']
add_time(x, dt118up, a5)

conver_cvs(a = a6, b = data_1_21_naik)
dt121up = pd.read_csv(a6)
x = dt121up['jarak']
add_time(x, dt121up, a6)

conver_cvs(a = a7, b = data_1_24_naik)
dt124up = pd.read_csv(a7)
x = dt124up['jarak']
add_time(x, dt124up, a7)

conver_cvs(a = a8, b = data_1_27_naik)
dt127up = pd.read_csv(a8)
x = dt127up['jarak']
add_time(x, dt127up, a8)

conver_cvs(a = a9, b = data_1_30_naik)
dt130up = pd.read_csv(a9)
x = dt130up['jarak']
add_time(x, dt130up, a9)


conver_cvs(a = b1, b = data_1_6_turun)
dt16dw = pd.read_csv(b1)
x = dt16dw['jarak']
add_time(x, dt16dw, b1)

conver_cvs(a = b2, b = data_1_9_turun)
dt19dw = pd.read_csv(b2)
x = dt19dw['jarak']
add_time(x, dt19dw, b2)

conver_cvs(a = b3, b = data_1_12_turun)
dt112dw = pd.read_csv(b3)
x = dt112dw['jarak']
add_time(x, dt112dw, b3)

conver_cvs(a = b4, b = data_1_15_turun)
dt115dw = pd.read_csv(b4)
x = dt115dw['jarak']
add_time(x, dt115dw, b4)

conver_cvs(a = b5, b = data_1_18_turun)
dt118dw = pd.read_csv(b5)
x = dt118dw['jarak']
add_time(x, dt118dw, b5)

conver_cvs(a = b6, b = data_1_21_turun)
dt121dw = pd.read_csv(b6)
x = dt121dw['jarak']
add_time(x, dt121dw, b6)

conver_cvs(a = b7, b = data_1_24_turun)
dt124dw = pd.read_csv(b7)
x = dt124dw['jarak']
add_time(x, dt124dw, b7)

conver_cvs(a = b8, b = data_1_27_turun)
dt127dw = pd.read_csv(b8)
x = dt127dw['jarak']
add_time(x, dt127dw, b8)

# conver_cvs(a = b9, b = data_1_30_turun)
# dt130dw = pd.read_csv(b9)
# x = dt130dw['jarak']
# add_time(x, dt130dw)

# putaran kedua

conver_cvs(a = c1, b = data_2_6_naik)
dt216up = pd.read_csv(c1)
x = dt216up['jarak']
add_time(x, dt216up, c1)

conver_cvs(a = c2, b = data_2_9_naik)
dt219up = pd.read_csv(c2)
x = dt219up['jarak']
add_time(x, dt219up, c2)

conver_cvs(a = c3, b = data_2_12_naik)
dt212up = pd.read_csv(c3)
x = dt212up['jarak']
add_time(x, dt212up, c3)

conver_cvs(a = c4, b = data_2_15_naik)
dt215up = pd.read_csv(c4)
x = dt215up['jarak']
add_time(x, dt215up, c4)

conver_cvs(a = c5, b = data_2_18_naik)
dt218up = pd.read_csv(c5)
x = dt218up['jarak']
add_time(x, dt218up, c5)

conver_cvs(a = c6, b = data_2_21_naik)
dt221up = pd.read_csv(c6)
x = dt221up['jarak']
add_time(x, dt221up, c6)

conver_cvs(a = c7, b = data_2_24_naik)
dt224up = pd.read_csv(c7)
x = dt224up['jarak']
add_time(x, dt224up, c7)

conver_cvs(a = c8, b = data_2_27_naik)
dt227up = pd.read_csv(c8)
x = dt227up['jarak']
add_time(x, dt227up, c8)

conver_cvs(a = c9, b = data_2_30_naik)
dt230up = pd.read_csv(c9)
x = dt230up['jarak']
add_time(x, dt230up, c9)


conver_cvs(a = d1, b = data_2_6_turun)
dt36dw = pd.read_csv(d1)
x = dt36dw['jarak']
add_time(x, dt36dw, d1)

conver_cvs(a = d2, b = data_2_9_turun)
dt39dw = pd.read_csv(d2)
x = dt39dw['jarak']
add_time(x, dt39dw, d2)

conver_cvs(a = d3, b = data_2_12_turun)
dt312dw = pd.read_csv(d3)
x = dt312dw['jarak']
add_time(x, dt312dw, d3)

conver_cvs(a = d4, b = data_2_15_turun)
dt315dw = pd.read_csv(d4)
x = dt315dw['jarak']
add_time(x, dt315dw, d4)

conver_cvs(a = d5, b = data_2_18_turun)
dt318dw = pd.read_csv(d5)
x = dt318dw['jarak']
add_time(x, dt318dw, d5)

conver_cvs(a = d6, b = data_2_21_turun)
dt321dw = pd.read_csv(d6)
x = dt321dw['jarak']
add_time(x, dt321dw, d6)

conver_cvs(a = d7, b = data_2_24_turun)
dt324dw = pd.read_csv(d7)
x = dt324dw['jarak']
add_time(x, dt324dw, d7)

conver_cvs(a = d8, b = data_2_27_turun)
dt327dw = pd.read_csv(d8)
x = dt327dw['jarak']
add_time(x, dt327dw, d8)

conver_cvs(a = d9, b = data_2_30_turun)
dt330dw = pd.read_csv(d9)
x = dt330dw['jarak']
add_time(x, dt330dw, d9)


# putaran ketiga

conver_cvs(a = f1, b = data_3_6_naik)
dt16up = pd.read_csv(f1)
x = dt16up['jarak']
add_time(x, dt16up, f1)

conver_cvs(a = f2, b = data_3_9_naik)
dt19up = pd.read_csv(f2)
x = dt19up['jarak']
add_time(x, dt19up, f2)

conver_cvs(a = f3, b = data_3_12_naik)
dt112up = pd.read_csv(f3)
x = dt112up['jarak']
add_time(x, dt112up, f3)

conver_cvs(a = f4, b = data_3_15_naik)
dt115up = pd.read_csv(f4)
x = dt115up['jarak']
add_time(x, dt115up, f4)

conver_cvs(a = f5, b = data_3_18_naik)
dt118up = pd.read_csv(f5)
x = dt118up['jarak']
add_time(x, dt118up, f5)

conver_cvs(a = f6, b = data_3_21_naik)
dt121up = pd.read_csv(f6)
x = dt121up['jarak']
add_time(x, dt121up, f6)

conver_cvs(a = f7, b = data_3_24_naik)
dt124up = pd.read_csv(f7)
x = dt124up['jarak']
add_time(x, dt124up, f7)

conver_cvs(a = f8, b = data_3_27_naik)
dt127up = pd.read_csv(f8)
x = dt127up['jarak']
add_time(x, dt127up, f8)

conver_cvs(a = f9, b = data_3_30_naik)
dt130up = pd.read_csv(f9)
x = dt130up['jarak']
add_time(x, dt130up, f9)


conver_cvs(a = g1, b = data_3_6_turun)
dt16dw = pd.read_csv(g1)
x = dt16dw['jarak']
add_time(x, dt16dw, g1)

conver_cvs(a = g2, b = data_3_9_turun)
dt19dw = pd.read_csv(g2)
x = dt19dw['jarak']
add_time(x, dt19dw, g2)

conver_cvs(a = g3, b = data_3_12_turun)
dt112dw = pd.read_csv(g3)
x = dt112dw['jarak']
add_time(x, dt112dw, g3)

conver_cvs(a = g4, b = data_3_15_turun)
dt115dw = pd.read_csv(g4)
x = dt115dw['jarak']
add_time(x, dt115dw, g4)

conver_cvs(a = g5, b = data_3_18_turun)
dt118dw = pd.read_csv(g5)
x = dt118dw['jarak']
add_time(x, dt118dw, g5)

conver_cvs(a = g6, b = data_3_21_turun)
dt121dw = pd.read_csv(g6)
x = dt121dw['jarak']
add_time(x, dt121dw, g6)

conver_cvs(a = g7, b = data_3_24_turun)
dt124dw = pd.read_csv(g7)
x = dt124dw['jarak']
add_time(x, dt124dw, g7)

conver_cvs(a = g8, b = data_3_27_turun)
dt127dw = pd.read_csv(g8)
x = dt127dw['jarak']
add_time(x, dt127dw, g8)

conver_cvs(a = g9, b = data_3_30_turun)
dt130dw = pd.read_csv(g9)
x = dt130dw['jarak']
add_time(x, dt130dw, g9)
