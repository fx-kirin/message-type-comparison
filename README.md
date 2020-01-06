```
## cpu model:           Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz  # 2603.868 MHz
## parameters:          loop=100000, cycle=1, extra=0

##                                                      real    (total    = user    + sys)
cbor2.dump                                            0.2791    0.2800    0.2800    0.0000
message_pack                                          0.0100    0.0100    0.0100    0.0000
orjson                                                0.0304    0.0200    0.0200    0.0000
pickle 0                                              0.0013    0.0000    0.0000    0.0000
pickle 1                                              0.0015    0.0000    0.0000    0.0000
pickle 2                                              0.0010    0.0100    0.0100    0.0000
pickle 3                                              0.0008    0.0000    0.0000    0.0000
pickle 4                                              0.0007    0.0000    0.0000    0.0000

## Ranking                                              real
pickle 4                                              0.0007  (100.0) ********************
pickle 3                                              0.0008  ( 91.7) ******************
pickle 2                                              0.0010  ( 75.3) ***************
pickle 0                                              0.0013  ( 56.5) ***********
pickle 1                                              0.0015  ( 47.3) *********
message_pack                                          0.0100  (  7.2) *
orjson                                                0.0304  (  2.4)
cbor2.dump                                            0.2791  (  0.3)

## Matrix                                               real    [01]    [02]    [03]    [04]    [05]    [06]    [07]    [08]
[01] pickle 4                                         0.0007   100.0   109.1   132.8   177.0   211.6  1383.3  4188.4 38488.1
[02] pickle 3                                         0.0008    91.7   100.0   121.7   162.2   193.9  1267.8  3838.8 35275.0
[03] pickle 2                                         0.0010    75.3    82.1   100.0   133.3   159.3  1041.5  3153.5 28978.1
[04] pickle 0                                         0.0013    56.5    61.6    75.0   100.0   119.5   781.5  2366.2 21743.0
[05] pickle 1                                         0.0015    47.3    51.6    62.8    83.7   100.0   653.7  1979.3 18188.4
[06] message_pack                                     0.0100     7.2     7.9     9.6    12.8    15.3   100.0   302.8  2782.4
[07] orjson                                           0.0304     2.4     2.6     3.2     4.2     5.1    33.0   100.0   918.9
[08] cbor2.dump                                       0.2791     0.3     0.3     0.3     0.5     0.5     3.6    10.9   100.0

## benchmarker:         release 4.0.1 (for python)
## python version:      3.6.7
## python compiler:     GCC 7.3.0
## python platform:     Linux-4.15.0-72-generic-x86_64-with-debian-buster-sid
## python executable:   /home/zenbook/.cache/pypoetry/virtualenvs/message-type-comparison-cQ2MAnKK-py3.6/bin/python
## cpu model:           Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz  # 2306.771 MHz
## parameters:          loop=100000, cycle=1, extra=0

##                                                      real    (total    = user    + sys)
cbor2.dump                                            0.2843    0.2800    0.2800    0.0000
message_pack                                          0.0086    0.0200    0.0100    0.0100
orjson                                                0.0223    0.0200    0.0200    0.0000
pickle 0                                              0.0109    0.0100    0.0100    0.0000
pickle 1                                              0.0082    0.0100    0.0100    0.0000
pickle 2                                              0.0093    0.0100    0.0100    0.0000
pickle 3                                              0.0112    0.0100    0.0100    0.0000
pickle 4                                              0.0079    0.0000    0.0000    0.0000

## Ranking                                              real
pickle 4                                              0.0079  (100.0) ********************
pickle 1                                              0.0082  ( 96.7) *******************
message_pack                                          0.0086  ( 92.6) *******************
pickle 2                                              0.0093  ( 85.8) *****************
pickle 0                                              0.0109  ( 72.8) ***************
pickle 3                                              0.0112  ( 71.0) **************
orjson                                                0.0223  ( 35.6) *******
cbor2.dump                                            0.2843  (  2.8) *

## Matrix                                               real    [01]    [02]    [03]    [04]    [05]    [06]    [07]    [08]
[01] pickle 4                                         0.0079   100.0   103.4   108.0   116.5   137.3   140.9   280.7  3579.4
[02] pickle 1                                         0.0082    96.7   100.0   104.5   112.8   132.8   136.3   271.6  3463.0
[03] message_pack                                     0.0086    92.6    95.7   100.0   107.9   127.2   130.4   260.0  3314.9
[04] pickle 2                                         0.0093    85.8    88.7    92.6   100.0   117.8   120.9   240.9  3071.2
[05] pickle 0                                         0.0109    72.8    75.3    78.6    84.9   100.0   102.6   204.5  2606.8
[06] pickle 3                                         0.0112    71.0    73.4    76.7    82.7    97.5   100.0   199.3  2541.2
[07] orjson                                           0.0223    35.6    36.8    38.5    41.5    48.9    50.2   100.0  1275.0
[08] cbor2.dump                                       0.2843     2.8     2.9     3.0     3.3     3.8     3.9     7.8   100.0
```
