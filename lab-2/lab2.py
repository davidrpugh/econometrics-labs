# IPython log file

get_ipython().magic(u'pinfo %logstart')
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
from pandas.tools.plotting import scatter_matrix
# need to manually set the print options in order to get data to display
pd.set_printoptions(max_columns=99)
# load the data using same command as last time
mrw_1992_data = sm.iolib.foreign.genfromdta('mrw1992.dta', missing_flt=NaN, missing_str=NaN, pandas=True)
print type(mrw_1992_data)
# view the entire dataset
mrw_1992_data
#[Out]#      c_index             c_name c_code  cont  nonoil  inter  oecd  gdp60  gdp85  popgrowth       igdp  school
#[Out]# 0          1            Algeria    DZA     1       1      1     0   2485   4371        2.6  24.100000     4.5
#[Out]# 1          2             Angola    AGO     1       1      0     0   1588   1171        2.1   5.800000     1.8
#[Out]# 2          3              Benin    BEN     1       1      0     0   1116   1071        2.4  10.800000     1.8
#[Out]# 3          4           Botswana    BWA     1       1      1     0    959   3671        3.2  28.299999     2.9
#[Out]# 4          5       Burkina Faso    BFA     1       1      0     0    529    857        0.9  12.700000     0.4
#[Out]# 5          6            Burundi    BDI     1       1      0     0    755    663        1.7   5.100000     0.4
#[Out]# 6          7           Cameroon    CMR     1       1      1     0    889   2190        2.1  12.800000     3.4
#[Out]# 7          8  Central Afr. Rep.    CAF     1       1      0     0    838    789        1.7  10.500000     1.4
#[Out]# 8          9               Chad    TCD     1       1      0     0    908    462        1.9   6.900000     0.4
#[Out]# 9         10           PR Congo    RCB     1       1      0     0   1009   2624        2.4  28.799999     3.8
#[Out]# 10        11              Egypt    EGY     1       1      0     0    907   2160        2.5  16.299999     7.0
#[Out]# 11        12           Ethiopia    ETH     1       1      1     0    533    608        2.3   5.400000     1.1
#[Out]# 12        13              Gabon    GAB     1       0      0     0   1307   5350        1.4  22.100000     2.6
#[Out]# 13        14        Gambia, The    GMB     1       0      0     0    799    NaN        NaN  18.100000     1.5
#[Out]# 14        15              Ghana    GHA     1       1      0     0   1009    727        2.3   9.100000     4.7
#[Out]# 15        16             Guinea    GIN     1       0      0     0    746    869        1.6  10.900000     NaN
#[Out]# 16        17        Ivory Coast    CIV     1       1      1     0   1386   1704        4.3  12.400000     2.3
#[Out]# 17        18              Kenya    KEN     1       1      1     0    944   1329        3.4  17.400000     2.4
#[Out]# 18        19            Lesotho    LSO     1       0      0     0    431   1483        1.9  12.600000     2.0
#[Out]# 19        20            Liberia    LBR     1       1      0     0    863    944        3.0  21.500000     2.5
#[Out]# 20        21         Madagascar    MDG     1       1      1     0   1194    975        2.2   7.100000     2.6
#[Out]# 21        22             Malawi    MWI     1       1      1     0    455    823        2.4  13.200000     0.6
#[Out]# 22        23               Mali    MLI     1       1      1     0    737    710        2.2   7.300000     1.0
#[Out]# 23        24         Mauritania    MRT     1       1      0     0    777   1038        2.2  25.600000     1.0
#[Out]# 24        25          Mauritius    MUS     1       1      0     0   1973   2967        2.6  17.100000     7.3
#[Out]# 25        26            Morocco    MAR     1       1      1     0   1030   2348        2.5   8.300000     3.6
#[Out]# 26        27         Mozambique    MOZ     1       1      0     0   1420   1035        2.7   6.100000     0.7
#[Out]# 27        28              Niger    NER     1       1      0     0    539    841        2.6  10.300000     0.5
#[Out]# 28        29            Nigeria    NGA     1       1      1     0   1055   1186        2.4  12.000000     2.3
#[Out]# 29        30             Rwanda    RWA     1       1      0     0    460    696        2.8   7.900000     0.4
#[Out]# 30        31            Senegal    SEN     1       1      1     0   1392   1450        2.3   9.600000     1.7
#[Out]# 31        32       Sierra Leone    SLE     1       1      0     0    511    805        1.6  10.900000     1.7
#[Out]# 32        33            Somalia    SOM     1       1      0     0    901    657        3.1  13.800000     1.1
#[Out]# 33        34       South Africa    ZAF     1       1      1     0   4768   7064        2.3  21.600000     3.0
#[Out]# 34        35              Sudan    SDN     1       1      0     0   1254   1038        2.6  13.200000     2.0
#[Out]# 35        36          Swaziland    SWZ     1       0      0     0    817    NaN        NaN  17.700001     3.7
#[Out]# 36        37           Tanzania    TZA     1       1      1     0    383    710        2.9  18.000000     0.5
#[Out]# 37        38               Togo    TGO     1       1      0     0    777    978        2.5  15.500000     2.9
#[Out]# 38        39            Tunisia    TUN     1       1      1     0   1623   3661        2.4  13.800000     4.3
#[Out]# 39        40             Uganda    UGA     1       1      0     0    601    667        3.1   4.100000     1.1
#[Out]# 40        41              Zaire    ZAR     1       1      0     0    594    412        2.4   6.500000     3.6
#[Out]# 41        42             Zambia    ZMB     1       1      1     0   1410   1217        2.7  31.700001     2.4
#[Out]# 42        43           Zimbabwe    ZWE     1       1      1     0   1187   2107        2.8  21.100000     4.4
#[Out]# 43        44        Afghanistan    AFG     2       0      0     0   1224    NaN        NaN   6.900000     0.9
#[Out]# 44        45            Bahrain    BHR     2       0      0     0    NaN    NaN        NaN  30.000000    12.1
#[Out]# 45        46         Bangladesh    BGD     2       1      1     0    846   1221        2.6   6.800000     3.2
#[Out]# 46        47              Burma    MMR     2       1      1     0    517   1031        1.7  11.400000     3.5
#[Out]# 47        48          Hong Kong    HKG     2       1      1     0   3085  13372        3.0  19.900000     7.2
#[Out]# 48        49              India    IND     2       1      1     0    978   1339        2.4  16.799999     5.1
#[Out]# 49        50               Iran    IRN     2       0      0     0   3606   7400        3.4  18.400000     6.5
#[Out]# 50        51               Iraq    IRQ     2       0      0     0   4916   5626        3.2  16.200001     7.4
#[Out]# 51        52             Israel    ISR     2       1      1     0   4802  10450        2.8  28.500000     9.5
#[Out]# 52        53              Japan    JPN     2       1      1     1   3493  13893        1.2  36.000000    10.9
#[Out]# 53        54             Jordan    JOR     2       1      1     0   2183   4312        2.7  17.600000    10.8
#[Out]# 54        55        South Korea    KOR     2       1      1     0   1285   4775        2.7  22.299999    10.2
#[Out]# 55        56             Kuwait    KWT     2       0      0     0  77881  25635        6.8   9.500000     9.6
#[Out]# 56        57           Malaysia    MYS     2       1      1     0   2154   5788        3.2  23.200001     7.3
#[Out]# 57        58              Nepal    NPL     2       1      0     0    833    974        2.0   5.900000     2.3
#[Out]# 58        59               Oman    OMN     2       0      0     0    NaN  15584        3.3  15.600000     2.7
#[Out]# 59        60           Pakistan    PAK     2       1      1     0   1077   2175        3.0  12.200000     3.0
#[Out]# 60        61        Philippines    PHL     2       1      1     0   1668   2430        3.0  14.900000    10.6
#[Out]# 61        62       Saudi Arabia    SAU     2       0      0     0   6731  11057        4.1  12.800000     3.1
#[Out]# 62        63          Singapore    SGP     2       1      1     0   2793  14678        2.6  32.200001     9.0
#[Out]# 63        64          Sri Lanka    LKA     2       1      1     0   1794   2482        2.4  14.800000     8.3
#[Out]# 64        65              Syria    SYR     2       1      1     0   2382   6042        3.0  15.900000     8.8
#[Out]# 65        66             Taiwan    TWN     2       0      0     0    NaN    NaN        NaN  20.700001     NaN
#[Out]# 66        67           Thailand    THA     2       1      1     0   1308   3220        3.1  18.000000     4.4
#[Out]# 67        68   U. Arab Emirates    ARE     2       0      0     0    NaN  18513        NaN  26.500000     NaN
#[Out]# 68        69              Yemen    YEM     2       0      0     0    NaN   1918        2.5  17.200001     0.6
#[Out]# 69        70            Austria    AUT     3       1      1     1   5939  13327        0.4  23.400000     8.0
#[Out]# 70        71            Belgium    BEL     3       1      1     1   6789  14290        0.5  23.400000     9.3
#[Out]# 71        72             Cyprus    CYP     3       0      0     0   2948    NaN        NaN  31.200001     8.2
#[Out]# 72        73            Denmark    DNK     3       1      1     1   8551  16491        0.6  26.600000    10.7
#[Out]# 73        74            Finland    FIN     3       1      1     1   6527  13779        0.7  36.900002    11.5
#[Out]# 74        75             France    FRA     3       1      1     1   7215  15027        1.0  26.200001     8.9
#[Out]# 75        76       West Germany    DEU     3       1      1     1   7695  15297        0.5  28.500000     8.4
#[Out]# 76        77             Greece    GRC     3       1      1     1   2257   6868        0.7  29.299999     7.9
#[Out]# 77        78            Iceland    ISL     3       0      0     0   8091    NaN        NaN  29.000000    10.2
#[Out]# 78        79            Ireland    IRL     3       1      1     1   4411   8675        1.1  25.900000    11.4
#[Out]# 79        80              Italy    ITA     3       1      1     1   4913  11082        0.6  24.900000     7.1
#[Out]# 80        81         Luxembourg    LUX     3       0      0     0   9015    NaN        NaN  26.900000     5.0
#[Out]# 81        82              Malta    MLT     3       0      0     0   2293    NaN        NaN  30.900000     7.1
#[Out]# 82        83        Netherlands    NLD     3       1      1     1   7689  13177        1.4  25.799999    10.7
#[Out]# 83        84             Norway    NOR     3       1      1     1   7938  19723        0.7  29.100000    10.0
#[Out]# 84        85           Portugal    PRT     3       1      1     1   2272   5827        0.6  22.500000     5.8
#[Out]# 85        86              Spain    ESP     3       1      1     1   3766   9903        1.0  17.700001     8.0
#[Out]# 86        87             Sweden    SWE     3       1      1     1   7802  15237        0.4  24.500000     7.9
#[Out]# 87        88        Switzerland    CHE     3       1      1     1  10308  15881        0.8  29.700001     4.8
#[Out]# 88        89             Turkey    TUR     3       1      1     1   2274   4444        2.5  20.200001     5.5
#[Out]# 89        90     United Kingdom    GBR     3       1      1     1   7634  13331        0.3  18.400000     8.9
#[Out]# 90        91           Barbados    BRB     4       0      0     0   3165    NaN        NaN  19.500000    12.1
#[Out]# 91        92             Canada    CAN     4       1      1     1  10286  17935        2.0  23.299999    10.6
#[Out]# 92        93         Costa Rica    CRI     4       1      1     0   3360   4492        3.5  14.700000     7.0
#[Out]# 93        94      Dominican Rep    DOM     4       1      1     0   1939   3308        2.9  17.100000     5.8
#[Out]# 94        95        El Salvador    SLV     4       1      1     0   2042   1997        3.3   8.000000     3.9
#[Out]# 95        96          Guatemala    GTM     4       1      1     0   2481   3034        3.1   8.800000     2.4
#[Out]# 96        97              Haiti    HTI     4       1      1     0   1096   1237        1.3   7.100000     1.9
#[Out]# 97        98           Honduras    HND     4       1      1     0   1430   1822        3.1  13.800000     3.7
#[Out]# 98        99            Jamaica    JAM     4       1      1     0   2726   3080        1.6  20.600000    11.2
#[Out]# 99       100             Mexico    MEX     4       1      1     0   4229   7380        3.3  19.500000     6.6
#[Out]# 100      101          Nicaragua    NIC     4       1      1     0   3195   3978        3.3  14.500000     5.8
#[Out]# 101      102             Panama    PAN     4       1      1     0   2423   5021        3.0  26.100000    11.6
#[Out]# 102      103  Trinidad & Tobago    TTO     4       1      1     0   9253  11285        1.9  20.400000     8.8
#[Out]# 103      104                USA    USA     4       1      1     1  12362  18988        1.5  21.100000    11.9
#[Out]# 104      105          Argentina    ARG     5       1      1     0   4852   5533        1.5  25.299999     5.0
#[Out]# 105      106            Bolivia    BOL     5       1      1     0   1618   2055        2.4  13.300000     4.9
#[Out]# 106      107             Brazil    BRA     5       1      1     0   1842   5563        2.9  23.200001     4.7
#[Out]# 107      108              Chile    CHL     5       1      1     0   5189   5533        2.3  29.700001     7.7
#[Out]# 108      109           Colombia    COL     5       1      1     0   2672   4405        3.0  18.000000     6.1
#[Out]# 109      110            Ecuador    ECU     5       1      1     0   2198   4504        2.8  24.400000     7.2
#[Out]# 110      111             Guyana    GUY     5       0      0     0   2761    NaN        NaN  32.400002    11.7
#[Out]# 111      112           Paraguay    PRY     5       1      1     0   1951   3914        2.7  11.700000     4.4
#[Out]# 112      113               Peru    PER     5       1      1     0   3310   3775        2.9  12.000000     8.0
#[Out]# 113      114            Surinam    SUR     5       0      0     0   3226    NaN        NaN  19.400000     8.1
#[Out]# 114      115            Uruguay    URY     5       1      1     0   5119   5495        0.6  11.800000     7.0
#[Out]# 115      116          Venezuela    VEN     5       1      1     0  10367   6336        3.8  11.400000     7.0
#[Out]# 116      117          Australia    AUS     6       1      1     1   8440  13409        2.0  31.500000     9.8
#[Out]# 117      118               Fiji    FJI     6       0      0     0   3634    NaN        NaN  20.600000     8.1
#[Out]# 118      119          Indonesia    IDN     6       1      1     0    879   2159        1.9  13.900000     4.1
#[Out]# 119      120        New Zealand    NZL     6       1      1     1   9523  12308        1.7  22.500000    11.9
#[Out]# 120      121   Papua New Guinea    PNG     6       1      0     0   1781   2544        2.1  16.200001     1.5
# summarize
mrw_1992_data.describe()
#[Out]#           c_index        cont      nonoil       inter        oecd         gdp60         gdp85   popgrowth        igdp      school
#[Out]# count  121.000000  121.000000  121.000000  121.000000  121.000000    116.000000    108.000000  107.000000  121.000000  118.000000
#[Out]# mean    61.000000    2.512397    0.809917    0.619835    0.181818   3681.818966   5683.259259    2.279439   18.157025    5.526271
#[Out]# std     35.073732    1.517211    0.393998    0.487446    0.387298   7492.877637   5688.670819    0.998748    7.853310    3.532037
#[Out]# min      1.000000    1.000000    0.000000    0.000000    0.000000    383.000000    412.000000    0.300000    4.100000    0.400000
#[Out]# 25%     31.000000    1.000000    1.000000    0.000000    0.000000    973.250000   1209.250000    1.700000   12.000000    2.400000
#[Out]# 50%     61.000000    2.000000    1.000000    1.000000    0.000000   1962.000000   3484.500000    2.400000   17.700001    4.950000
#[Out]# 75%     91.000000    4.000000    1.000000    1.000000    0.000000   4274.500000   7718.750000    2.900000   24.100000    8.175000
#[Out]# max    121.000000    6.000000    1.000000    1.000000    1.000000  77881.000000  25635.000000    6.800000   36.900002   12.100000
# create some new variables using the natural logarithm function from NumPy
mrw_1992_data_nonoil['lngdp60'] = np.log(mrw_1992_data_nonoil['gdp60'])
mrw_1992_data_nonoil['lngdp85'] = np.log(mrw_1992_data_nonoil['gdp85'])
# remove the oil exporters from the analysis
mrw_1992_data_nonoil = mrw_1992_data[mrw_1992_data['nonoil'] == 1]
mrw_1992_data_nonoil 
#[Out]#      c_index             c_name c_code  cont  nonoil  inter  oecd  gdp60  gdp85  popgrowth       igdp  school
#[Out]# 0          1            Algeria    DZA     1       1      1     0   2485   4371        2.6  24.100000     4.5
#[Out]# 1          2             Angola    AGO     1       1      0     0   1588   1171        2.1   5.800000     1.8
#[Out]# 2          3              Benin    BEN     1       1      0     0   1116   1071        2.4  10.800000     1.8
#[Out]# 3          4           Botswana    BWA     1       1      1     0    959   3671        3.2  28.299999     2.9
#[Out]# 4          5       Burkina Faso    BFA     1       1      0     0    529    857        0.9  12.700000     0.4
#[Out]# 5          6            Burundi    BDI     1       1      0     0    755    663        1.7   5.100000     0.4
#[Out]# 6          7           Cameroon    CMR     1       1      1     0    889   2190        2.1  12.800000     3.4
#[Out]# 7          8  Central Afr. Rep.    CAF     1       1      0     0    838    789        1.7  10.500000     1.4
#[Out]# 8          9               Chad    TCD     1       1      0     0    908    462        1.9   6.900000     0.4
#[Out]# 9         10           PR Congo    RCB     1       1      0     0   1009   2624        2.4  28.799999     3.8
#[Out]# 10        11              Egypt    EGY     1       1      0     0    907   2160        2.5  16.299999     7.0
#[Out]# 11        12           Ethiopia    ETH     1       1      1     0    533    608        2.3   5.400000     1.1
#[Out]# 14        15              Ghana    GHA     1       1      0     0   1009    727        2.3   9.100000     4.7
#[Out]# 16        17        Ivory Coast    CIV     1       1      1     0   1386   1704        4.3  12.400000     2.3
#[Out]# 17        18              Kenya    KEN     1       1      1     0    944   1329        3.4  17.400000     2.4
#[Out]# 19        20            Liberia    LBR     1       1      0     0    863    944        3.0  21.500000     2.5
#[Out]# 20        21         Madagascar    MDG     1       1      1     0   1194    975        2.2   7.100000     2.6
#[Out]# 21        22             Malawi    MWI     1       1      1     0    455    823        2.4  13.200000     0.6
#[Out]# 22        23               Mali    MLI     1       1      1     0    737    710        2.2   7.300000     1.0
#[Out]# 23        24         Mauritania    MRT     1       1      0     0    777   1038        2.2  25.600000     1.0
#[Out]# 24        25          Mauritius    MUS     1       1      0     0   1973   2967        2.6  17.100000     7.3
#[Out]# 25        26            Morocco    MAR     1       1      1     0   1030   2348        2.5   8.300000     3.6
#[Out]# 26        27         Mozambique    MOZ     1       1      0     0   1420   1035        2.7   6.100000     0.7
#[Out]# 27        28              Niger    NER     1       1      0     0    539    841        2.6  10.300000     0.5
#[Out]# 28        29            Nigeria    NGA     1       1      1     0   1055   1186        2.4  12.000000     2.3
#[Out]# 29        30             Rwanda    RWA     1       1      0     0    460    696        2.8   7.900000     0.4
#[Out]# 30        31            Senegal    SEN     1       1      1     0   1392   1450        2.3   9.600000     1.7
#[Out]# 31        32       Sierra Leone    SLE     1       1      0     0    511    805        1.6  10.900000     1.7
#[Out]# 32        33            Somalia    SOM     1       1      0     0    901    657        3.1  13.800000     1.1
#[Out]# 33        34       South Africa    ZAF     1       1      1     0   4768   7064        2.3  21.600000     3.0
#[Out]# 34        35              Sudan    SDN     1       1      0     0   1254   1038        2.6  13.200000     2.0
#[Out]# 36        37           Tanzania    TZA     1       1      1     0    383    710        2.9  18.000000     0.5
#[Out]# 37        38               Togo    TGO     1       1      0     0    777    978        2.5  15.500000     2.9
#[Out]# 38        39            Tunisia    TUN     1       1      1     0   1623   3661        2.4  13.800000     4.3
#[Out]# 39        40             Uganda    UGA     1       1      0     0    601    667        3.1   4.100000     1.1
#[Out]# 40        41              Zaire    ZAR     1       1      0     0    594    412        2.4   6.500000     3.6
#[Out]# 41        42             Zambia    ZMB     1       1      1     0   1410   1217        2.7  31.700001     2.4
#[Out]# 42        43           Zimbabwe    ZWE     1       1      1     0   1187   2107        2.8  21.100000     4.4
#[Out]# 45        46         Bangladesh    BGD     2       1      1     0    846   1221        2.6   6.800000     3.2
#[Out]# 46        47              Burma    MMR     2       1      1     0    517   1031        1.7  11.400000     3.5
#[Out]# 47        48          Hong Kong    HKG     2       1      1     0   3085  13372        3.0  19.900000     7.2
#[Out]# 48        49              India    IND     2       1      1     0    978   1339        2.4  16.799999     5.1
#[Out]# 51        52             Israel    ISR     2       1      1     0   4802  10450        2.8  28.500000     9.5
#[Out]# 52        53              Japan    JPN     2       1      1     1   3493  13893        1.2  36.000000    10.9
#[Out]# 53        54             Jordan    JOR     2       1      1     0   2183   4312        2.7  17.600000    10.8
#[Out]# 54        55        South Korea    KOR     2       1      1     0   1285   4775        2.7  22.299999    10.2
#[Out]# 56        57           Malaysia    MYS     2       1      1     0   2154   5788        3.2  23.200001     7.3
#[Out]# 57        58              Nepal    NPL     2       1      0     0    833    974        2.0   5.900000     2.3
#[Out]# 59        60           Pakistan    PAK     2       1      1     0   1077   2175        3.0  12.200000     3.0
#[Out]# 60        61        Philippines    PHL     2       1      1     0   1668   2430        3.0  14.900000    10.6
#[Out]# 62        63          Singapore    SGP     2       1      1     0   2793  14678        2.6  32.200001     9.0
#[Out]# 63        64          Sri Lanka    LKA     2       1      1     0   1794   2482        2.4  14.800000     8.3
#[Out]# 64        65              Syria    SYR     2       1      1     0   2382   6042        3.0  15.900000     8.8
#[Out]# 66        67           Thailand    THA     2       1      1     0   1308   3220        3.1  18.000000     4.4
#[Out]# 69        70            Austria    AUT     3       1      1     1   5939  13327        0.4  23.400000     8.0
#[Out]# 70        71            Belgium    BEL     3       1      1     1   6789  14290        0.5  23.400000     9.3
#[Out]# 72        73            Denmark    DNK     3       1      1     1   8551  16491        0.6  26.600000    10.7
#[Out]# 73        74            Finland    FIN     3       1      1     1   6527  13779        0.7  36.900002    11.5
#[Out]# 74        75             France    FRA     3       1      1     1   7215  15027        1.0  26.200001     8.9
#[Out]# 75        76       West Germany    DEU     3       1      1     1   7695  15297        0.5  28.500000     8.4
#[Out]# 76        77             Greece    GRC     3       1      1     1   2257   6868        0.7  29.299999     7.9
#[Out]# 78        79            Ireland    IRL     3       1      1     1   4411   8675        1.1  25.900000    11.4
#[Out]# 79        80              Italy    ITA     3       1      1     1   4913  11082        0.6  24.900000     7.1
#[Out]# 82        83        Netherlands    NLD     3       1      1     1   7689  13177        1.4  25.799999    10.7
#[Out]# 83        84             Norway    NOR     3       1      1     1   7938  19723        0.7  29.100000    10.0
#[Out]# 84        85           Portugal    PRT     3       1      1     1   2272   5827        0.6  22.500000     5.8
#[Out]# 85        86              Spain    ESP     3       1      1     1   3766   9903        1.0  17.700001     8.0
#[Out]# 86        87             Sweden    SWE     3       1      1     1   7802  15237        0.4  24.500000     7.9
#[Out]# 87        88        Switzerland    CHE     3       1      1     1  10308  15881        0.8  29.700001     4.8
#[Out]# 88        89             Turkey    TUR     3       1      1     1   2274   4444        2.5  20.200001     5.5
#[Out]# 89        90     United Kingdom    GBR     3       1      1     1   7634  13331        0.3  18.400000     8.9
#[Out]# 91        92             Canada    CAN     4       1      1     1  10286  17935        2.0  23.299999    10.6
#[Out]# 92        93         Costa Rica    CRI     4       1      1     0   3360   4492        3.5  14.700000     7.0
#[Out]# 93        94      Dominican Rep    DOM     4       1      1     0   1939   3308        2.9  17.100000     5.8
#[Out]# 94        95        El Salvador    SLV     4       1      1     0   2042   1997        3.3   8.000000     3.9
#[Out]# 95        96          Guatemala    GTM     4       1      1     0   2481   3034        3.1   8.800000     2.4
#[Out]# 96        97              Haiti    HTI     4       1      1     0   1096   1237        1.3   7.100000     1.9
#[Out]# 97        98           Honduras    HND     4       1      1     0   1430   1822        3.1  13.800000     3.7
#[Out]# 98        99            Jamaica    JAM     4       1      1     0   2726   3080        1.6  20.600000    11.2
#[Out]# 99       100             Mexico    MEX     4       1      1     0   4229   7380        3.3  19.500000     6.6
#[Out]# 100      101          Nicaragua    NIC     4       1      1     0   3195   3978        3.3  14.500000     5.8
#[Out]# 101      102             Panama    PAN     4       1      1     0   2423   5021        3.0  26.100000    11.6
#[Out]# 102      103  Trinidad & Tobago    TTO     4       1      1     0   9253  11285        1.9  20.400000     8.8
#[Out]# 103      104                USA    USA     4       1      1     1  12362  18988        1.5  21.100000    11.9
#[Out]# 104      105          Argentina    ARG     5       1      1     0   4852   5533        1.5  25.299999     5.0
#[Out]# 105      106            Bolivia    BOL     5       1      1     0   1618   2055        2.4  13.300000     4.9
#[Out]# 106      107             Brazil    BRA     5       1      1     0   1842   5563        2.9  23.200001     4.7
#[Out]# 107      108              Chile    CHL     5       1      1     0   5189   5533        2.3  29.700001     7.7
#[Out]# 108      109           Colombia    COL     5       1      1     0   2672   4405        3.0  18.000000     6.1
#[Out]# 109      110            Ecuador    ECU     5       1      1     0   2198   4504        2.8  24.400000     7.2
#[Out]# 111      112           Paraguay    PRY     5       1      1     0   1951   3914        2.7  11.700000     4.4
#[Out]# 112      113               Peru    PER     5       1      1     0   3310   3775        2.9  12.000000     8.0
#[Out]# 114      115            Uruguay    URY     5       1      1     0   5119   5495        0.6  11.800000     7.0
#[Out]# 115      116          Venezuela    VEN     5       1      1     0  10367   6336        3.8  11.400000     7.0
#[Out]# 116      117          Australia    AUS     6       1      1     1   8440  13409        2.0  31.500000     9.8
#[Out]# 118      119          Indonesia    IDN     6       1      1     0    879   2159        1.9  13.900000     4.1
#[Out]# 119      120        New Zealand    NZL     6       1      1     1   9523  12308        1.7  22.500000    11.9
#[Out]# 120      121   Papua New Guinea    PNG     6       1      0     0   1781   2544        2.1  16.200001     1.5
# good idea to summarize the data after such a major change!
mrw_1992_data_nonoil.describe()
#[Out]#           c_index       cont  nonoil      inter       oecd         gdp60         gdp85  popgrowth       igdp     school
#[Out]# count   98.000000  98.000000      98  98.000000  98.000000     98.000000     98.000000  98.000000  98.000000  98.000000
#[Out]# mean    60.877551   2.520408       1   0.765306   0.224490   2994.897959   5309.765306   2.201020  17.672449   5.396939
#[Out]# std     36.190864   1.554704       0   0.425986   0.419391   2862.521970   5277.182620   0.889862   7.918330   3.468992
#[Out]# min      1.000000   1.000000       1   0.000000   0.000000    383.000000    412.000000   0.300000   4.100000   0.400000
#[Out]# 25%     29.250000   1.000000       1   1.000000   0.000000    963.750000   1174.750000   1.700000  11.725000   2.400000
#[Out]# 50%     60.500000   2.000000       1   1.000000   0.000000   1818.000000   3150.000000   2.400000  17.100000   4.750000
#[Out]# 75%     93.750000   4.000000       1   1.000000   0.000000   4113.250000   7015.000000   2.875000  23.400000   8.000000
#[Out]# max    121.000000   6.000000       1   1.000000   1.000000  12362.000000  19723.000000   4.300000  36.900002  11.900000
# create new variables using the natural logarithm function from NumPy
mrw_1992_data_nonoil['lngdp60'] = np.log(mrw_1992_data_nonoil['gdp60'])
mrw_1992_data_nonoil['lngdp85'] = np.log(mrw_1992_data_nonoil['gdp85'])
# summarize the newly created variables...
mrw_1992_data_nonoil.lngdp60.describe()
#[Out]# count    98.000000
#[Out]# mean      7.597921
#[Out]# std       0.901418
#[Out]# min       5.948035
#[Out]# 25%       6.870796
#[Out]# 50%       7.505405
#[Out]# 75%       8.320733
#[Out]# max       9.422383
mrw_1992_data_nonoil.lngdp85.describe()
#[Out]# count    98.000000
#[Out]# mean      8.047911
#[Out]# std       1.079392
#[Out]# min       6.021023
#[Out]# 25%       7.068795
#[Out]# 50%       8.054911
#[Out]# 75%       8.855732
#[Out]# max       9.889541
# generate the growth rate variable
mrw_1992_data_nonoil['growth'] = (mrw_1992_data_nonoil['lngdp85'] - mrw_1992_data_nonoil['lngdp60']) / 25.
# our endogenous (or dependent or response variable) is growth
y = mrw_1992_data_nonoil['growth']

# our matrix of exogenous (or independent variables) are a constant and lngdp60
X = sm.add_constant(mrw_1992_data_nonoil['lngdp60'], prepend=True)

# run the regression
results = sm.OLS(endog=y, exog=X).fit()

# examine the output
print results.summary()
# examine the output
print results.summary()
# get estimated coefficients for each regressor
results.params
#[Out]# const     -0.010663
#[Out]# lngdp60    0.003772
# get the default standard errors for each regressor
results.bse
#[Out]# const      0.015184
#[Out]# lngdp60    0.001985
# get the t-statistics for each regressor
results.tvalues
#[Out]# const     -0.702251
#[Out]# lngdp60    1.900771
# get the p-values for the standard significance test of each regressor
results.pvalues
#[Out]# const      0.484222
#[Out]# lngdp60    0.060332
# get 95% confidence intervals for each regressor 
results.conf_int(alpha=0.05)
#[Out]#                 0         1
#[Out]# const   -0.040803  0.019477
#[Out]# lngdp60 -0.000167  0.007712
# summarize growth
mrw_1992_data_nonoil.growth.describe()
#[Out]# count    98.000000
#[Out]# mean      0.018000
#[Out]# std       0.017856
#[Out]# min      -0.027027
#[Out]# 25%       0.005260
#[Out]# 50%       0.017987
#[Out]# 75%       0.029297
#[Out]# max       0.066369
# summarize log GDP per capita in 1960
mrw_1992_data_nonoil.lngdp60.describe()
#[Out]# count    98.000000
#[Out]# mean      7.597921
#[Out]# std       0.901418
#[Out]# min       5.948035
#[Out]# 25%       6.870796
#[Out]# 50%       7.505405
#[Out]# 75%       8.320733
#[Out]# max       9.422383
# get 95% confidence intervals for each regressor 
results.conf_int(alpha=0.05)
#[Out]#                 0         1
#[Out]# const   -0.040803  0.019477
#[Out]# lngdp60 -0.000167  0.007712
# get the t-statistics for each regressor
results.tvalues
#[Out]# const     -0.702251
#[Out]# lngdp60    1.900771
# get the p-values for the standard significance test of each regressor
results.pvalues
#[Out]# const      0.484222
#[Out]# lngdp60    0.060332
# create a new variable representing the de-meaned lngdp60
mrw_1992_data_nonoil['lngdp60_c'] = mrw_1992_data_nonoil['lngdp60'] - mrw_1992_data_nonoil.lngdp60.mean()
# compare lngdp60...
mrw_1992_data_nonoil.lngdp60.describe()
#[Out]# count    98.000000
#[Out]# mean      7.597921
#[Out]# std       0.901418
#[Out]# min       5.948035
#[Out]# 25%       6.870796
#[Out]# 50%       7.505405
#[Out]# 75%       8.320733
#[Out]# max       9.422383
#...with its de-meanded counterpart 
mrw_1992_data_nonoil.lngdp60_c.describe()
#[Out]# count    98.000000
#[Out]# mean     -0.000000
#[Out]# std       0.901418
#[Out]# min      -1.649886
#[Out]# 25%      -0.727126
#[Out]# 50%      -0.092516
#[Out]# 75%       0.722811
#[Out]# max       1.824461
# run the regression
X = sm.add_constant(mrw_1992_data_nonoil['lngdp60_c'], prepend=True)
results2 = sm.OLS(endog=y, exog=X).fit()

# examine the output
print results2.summary()
# get the r-squared of the regression
results.rsquared
#[Out]# 0.036269686284356339
# get the first few fitted values 
results.fittedvalues.head()
#[Out]# 0    0.018830
#[Out]# 1    0.017141
#[Out]# 2    0.015810
#[Out]# 3    0.015238
#[Out]# 4    0.012994
# get the first few residuals
results.resid.head()
#[Out]# 0    0.003759
#[Out]# 1   -0.029325
#[Out]# 2   -0.017456
#[Out]# 3    0.038455
#[Out]# 4    0.006304
# compare the hand calculation for R-squared
results.ess / results.centered_tss
#[Out]# 0.036269686284356374
# with the actual R-squared
results.rsquared
#[Out]# 0.036269686284356339
# dfs for the model (i.e., numerator of the F-test)
results.df_model
#[Out]# 1.0
# dfs for the model (i.e., denominator of the F-test)
results.df_resid
#[Out]# 96.0
# test statistic for the standard F test
results.fvalue
#[Out]# 3.6129297104641784
# p-value for the standard F-test
results.f_pvalue
#[Out]# 0.060331932950113985
# computes the RMSE using the residual sum of squares
np.sqrt((1 / 96.) * results.ssr)
#[Out]# 0.01761994468254471
# Recall we can get the total sum of square as follows
print 'TSS = %f' % results.centered_tss
# We can get the model sum of squares and the residual sum of squares
print 'MSS + RSS = %f' % (results.ess + results.ssr)
# model degrees of freedom = K - 1
results.df_model
#[Out]# 1.0
# residual degrees of freedom = N - K
results.df_resid
#[Out]# 96.0
# compare this ratio with...
results.ess / results.df_model
#[Out]# 0.0011216790118138316
# the model MSE...should be identical
results.mse_model
#[Out]# 0.0011216790118138316
# sqrt(residual MSE) should equal RMSE from above
np.sqrt(results.mse_resid)
#[Out]# 0.01761994468254471
# RMSE from above
np.sqrt(results.ssr / results.df_resid)
#[Out]# 0.01761994468254471
# our endogenous (or dependent or response variable) is growth
y = mrw_1992_data_nonoil['growth']

# our matrix of exogenous (or independent variables) are a constant and lngdp60
X = sm.add_constant(mrw_1992_data_nonoil[['lngdp60', 'popgrowth', 'igdp', 'school']], prepend=True)

# run the regression
results3 = sm.OLS(endog=y, exog=X).fit()

# examine the output
print results3.summary()
results3.params['lngdp60']
#[Out]# -0.010998473691909205
# compare confidence intervals...
results.conf_int(alpha=0.05)
#[Out]#                 0         1
#[Out]# const   -0.040803  0.019477
#[Out]# lngdp60 -0.000167  0.007712
# confidence interval for lngdp60 now excludes zero!
results3.conf_int(alpha=0.05)
#[Out]#                   0         1
#[Out]# const      0.030785  0.102946
#[Out]# lngdp60   -0.016044 -0.005953
#[Out]# popgrowth -0.004288  0.002453
#[Out]# igdp       0.000843  0.001759
#[Out]# school     0.001221  0.003869
# t-stat is no very large and negative...
results3.tvalues['lngdp60']
#[Out]# -4.3285446138199779
#...and highly significant!
results3.pvalues['lngdp60']
#[Out]# 3.7789632696439484e-05
# test statistic is large...
results3.fvalue
#[Out]# 19.228259900059548
# and highly significant...we could have guessed this by looking at the individual t-stats
results3.f_pvalue
#[Out]# 1.4869590895295668e-11
# the numerator degrees of freedom for the F-test is K - 1
results3.df_model
#[Out]# 4.0
# the denominator degrees of freedom for the F-test is N - K
results3.df_resid
#[Out]# 93.0
# adjusted R-squares is higher for multiple regression...
print "Adjusted R-square for simple bi-variate regression: ", results.rsquared_adj
print "Adjusted R-square for multiple regression: ", results3.rsquared_adj
# and RMSE is lower!
print "RMSE for simple bi-variate regression: ", np.sqrt(results.ssr / results.df_resid)
print "RMSE for multiple regression: ", np.sqrt(results3.ssr / results3.df_resid)
# coefficient on population growth is negative
results3.params['popgrowth']
#[Out]# -0.00091787349983282458
# fail to reject null hypothesis that coefficient is zero!
print "t-stat: ", results3.tvalues['popgrowth']
print "p-value: ", results3.pvalues['popgrowth']
# fail to reject null hypothesis that coefficient is zero!
print "t-stat: ", results3.tvalues['popgrowth']
print "p-value: ", results3.pvalues['popgrowth']
# coefficient on igdp is positive
results3.params['igdp']
#[Out]# 0.0013007163042079517
# reject null hypothesis that coefficient is zero!
print "t-stat: ", results3.tvalues['igdp']
print "p-value: ", results3.pvalues['igdp']
# coefficient on school is positive
results3.params['school']
#[Out]# 0.0025446475919545866
# reject null hypothesis that coefficient is zero!
print "t-stat: ", results3.tvalues['school']
print "p-value: ", results3.pvalues['school']
fig = plt.figure()
ax = fig.add_subplot(111)

X = mrw_1992_data_nonoil.lngdp60.values
Y = mrw_1992_data_nonoil.growth.values

# the scatterplot
ax.scatter(X, Y, color='orange', marker='o')

# doesn't seem to be a command to plot a line using slope and intercept!
grid = np.linspace(5, 10.5, 1000)
ax.plot(grid, results.params['lngdp60'] * grid + results.params['const'], color='red', label='OLS')

ax.set_xlim(5.5, 10.5)
ax.set_xlabel('log real GDP per worker (1960)')
ax.set_ylabel('Average growth in GDP 1960-1985')
ax.set_title('Divergence of GDP per worker?')

ax.legend(loc='best', frameon=False)

plt.savefig('Divergence of GDP per worker.png')
plt.show()
# end logging!
get_ipython().magic(u'logstop')
