# NRTU
### Key Generation:

- Choose a parameter n, which determines the size of the keys.
- Choose two random polynomials f and g, of degree n-1, with coefficients in the set {-1, 0, 1}.
- Ensure that f and g are invertible in the ring of polynomials modulo q, where q is a power of 2.
- Compute the polynomial h as the product of f and g.
- Choose a random polynomial t of degree n-1, with coefficients in the set {0, 1}.
- Compute the public key h*t mod q.
- The private key is g.
### Encryption:
- Convert the plaintext message to a polynomial m(x) of degree at most n-1.
- Choose a random polynomial r(x) of degree at most n-1, with coefficients in the set {0, 1}.
- Compute the ciphertext polynomial c(x) as (h*r + m) mod q.
### Decryption:
- Multiply the ciphertext polynomial c(x) by the private key g(x) to obtain c(x)*g(x).
- Reduce c(x)*g(x) modulo q to obtain e(x).
- Recover the message polynomial m(x) by subtracting e(x) from c(x) and reducing modulo p, where p is a small prime.
- Convert m(x) to the plaintext message.


```
Public key: [0, -1, -2, -2047, -2046, -2, 2042, -2050, -8187, -6145, -2052, -11, -12279, -12286, -8187, 2034, -10228, -18424, -16371, -4106, -4090, -12285, -20467, -12293, -14326, -6139, -16359, -10244, -18428, -12282, -10218, -12268, -6173, -16407, -16376, -12293, -8205, -6187, -12304, -16378, -14309, -12295, -8212, -14343, -10243, -14314, -12305, -10269, -20481, -2059, -16386, -12281, -20486, -26563, -20466, -12299, -20457, -30663, -22540, -18438, -20508, -36831, -30707, -26616, -30709, -36871, -12346, -38872, -47062, -36883, -26649, -26623, -51203, -45088, -55271, -32767, -40949, -43027, -49124, -34863, -38936, -43031, -36864, -36888, -59351, -45048, -47052, -40952, -49172, -67508, -43025, -40979, -30759, -38942, -49157, -41015, -32787, -34797, -57334, -40986, -51119, -42959, -42962, -20590, -49139, -55279, -49090, -10314, -34811, -16469, -22557, -42972, -38936, -38941, -28700, -49102, -36896, -51161, -36934, -38915, -45108, -59337, -38970, -30733, -41021, -61415, -36883, -26652, -43010, -59378, -69542, -47125, -59296, -65519, -47127, -59268, -32776, -41046, -45112, -57326, -51176, -51231, -37025, -59341, -59450, -87974, -81907, -63467, -49282, -77781, -71680, -47181, -79868, -57349, -65520, -63542, -87964, -69654, -92042, -55397, -73562, -83867, -98181, -63552, -81878, -77779, -83881, -51334, -63496, -61386, -85931, -75766, -37108, -81894, -98227, -65561, -75784, -81995, -55401, -83921, -85919, -63606, -81981, -92110, -81840, -73748, -71654, -63607, -102358, -100237, -71726, -77804, -102367, -104280, -86039, -94037, -108469, -108447, -96230, -89998, -67812, -94172, -69729, -67580, -96242, -82017, -110537, -128864, -84130, -92249, -92011, -77928, -79979, -86058, -102259, -90156, -110506, -100307, -112455, -81797, -124704, -90229, -106380, -106439, -108475, -104449, -110559, -100391, -145162, -143136, -84142, -94338, -135022, -112632, -114680, -84153, -100545, -114625, -102480, -118809, -145316, -104511, -110655, -122917, -78037, -102529, -118776, -129067, -108781, -118904, -120823, -118845, -114746, -106459, -82255, -114496, -84117, -86305, -133203, -118667, -110586, -124891, -90358, -77898, -141278, -116762, -84201, -112588, -112701, -129152, -137189, -126991, -110567, -141292, -141220, -129150, -133123, -127051, -135117, -149521, -183952, -127037, -128902, -133154, -119027, -163781, -153449, -84293, -143359, -137396, -112854, -167845, -180033, -137425, -153541, -137200, -129090, -145386, -149723, -159774, -167883, -184148, -141468, -145513, -184019, -180184, -123135, -110831, -155821, -135192, -141518, -151699, -127271, -174020, -172044, -192355, -184064, -137563, -149838, -192396, -135524, -137371, -151791, -157784, -166047, -229140, -137412, -172141, -178283, -204743, -198667, -182107, -141632, -155882, -186281, -171939, -174057, -174157, -163815, -172076, -178209, -180324, -166029, -180179, -161826, -168159, -190521, -145683, -188204, -155709, -184168, -131610, -159812, -167915, -170020, -190452, -155802, -190586, -186352, -196634, -208864, -174277, -196517, -186490, -182192, -161895, -170140, -204666, -198488, -204645, -215096, -145770, -163993, -192462, -209092, -202870, -206702, -155803, -184367, -204689, -147731, -215001, -164100, -155713, -166282, -206821, -190752, -265890, -208893, -218829, -241450, -231121, -200718, -204539, -229106, -180394, -208775, -196470, -192484, -192592, -239468, -210998, -211015, -225352, -202767, -172472, -271785, -160230, -211055, -204923, -198760, -196712, -205002, -210892, -200758, -251842, -194689, -158102, -229163, -213191, -224984, -247608, -247624, -190794, -209128, -233547, -200686, -253594, -213116, -205159, -270103, -237426, -204709, -241359, -225323, -225320, -267876, -237586, -195024, -251803, -272043, -251694, -239781, -255876, -203248, -253976, -280570, -245742, -252018, -247871, -223258, -237522, -290761, -223252, -274449, -329067, -201498, -257932, -288738, -247754, -296611, -199036, -252026, -231574, -268104, -200991, -231260, -237636, -260284, -266363, -270223, -252008, -263942, -247974, -237806, -219369, -217170, -231515, -304801, -270466, -251956, -270100, -258062, -229789, -251906, -256159, -237992, -241900, -280658, -284716, -320969, -284656, -241823, -251828, -286412, -268454, -280707, -262346, -227512, -278557, -264636, -262287, -295018, -304730, -207440, -253995, -270438, -294868, -257936, -286685, -240261, -288668, -294762, -268286, -266512, -270130, -248098, -231801, -282472, -218057, -284828, -304976, -288620, -264212, -244068, -246081, -225988, -262234, -248350, -300933, -258267, -270528, -248203, -292964, -278376, -247804, -258185, -249961, -266288, -272516, -278678, -284662, -339369, -266467, -235615, -288738, -221708, -231803, -274265, -258405, -270181, -284517, -278019, -270510, -315067, -264245, -284576, -278070, -193236, -250250, -256215, -310944, -265948, -274521, -317240, -321124, -337278, -303024, -250045, -251983, -252172, -272058, -286855, -248232, -235927, -321123, -280464, -264000, -272850, -268788, -248144, -241696, -288775, -288682, -258080, -264507, -260341, -286704, -260459, -248171, -327254, -309095, -233884, -233784, -282481, -278687, -321236, -288622, -315298, -270368, -272635, -311124, -303069, -266489, -313016, -310415, -266195, -248215, -301115, -244394, -304832, -286560, -248415, -310743, -316915, -311505, -286809, -319082, -290607, -282688, -278531, -228155, -242185, -292766, -292565, -266161, -302692, -301285, -268673, -323225, -315293, -266353, -282874, -284324, -235854, -292644, -266548, -319364, -286457, -303051, -238176, -262515, -315558, -266342, -286796, -284633, -260217, -263898, -288821, -242289, -355588, -287180, -242109, -256143, -270573, -246363, -272537, -310695, -264550, -262484, -215922, -284813, -296751, -333689, -289077, -231936, -296735, -288631, -310972, -299123, -242182, -282559, -333743, -290704, -319141, -323350, -290724, -304975, -272340, -242138, -299120, -290790, -290809, -244331, -289177, -248354, -276409, -335286, -284559, -319217, -286758, -274741, -292766, -272295, -260775, -321155, -315370, -258413, -256483, -272774, -301152, -319244, -274789, -254253, -250513, -307028, -296930, -286402, -310943, -222320, -278392, -300781, -248120, -293062, -290814, -272340, -337172, -327229, -272810, -242309, -290707, -311139, -266403, -264344, -275080, -305038, -286767, -282837, -264653, -327018, -276665, -300880, -308922, -272938, -282685, -300699, -317546, -323311, -298941, -264912, -325519, -296920, -284668, -268672, -280671, -297085, -242342, -247973, -311265, -306818, -300849, -280770, -284912, -295150, -274865, -252252, -268535, -266453, -307201, -290820, -292979, -280878, -299110, -299120, -268132, -300888, -227948, -258201, -268505, -325158, -296988, -300869, -252281, -306817, -278143, -281050, -232286, -308901, -286377, -278400, -294537, -292843, -300923, -294923, -306665, -301041, -325314, -240081, -300801, -327505, -307149, -310877, -380045, -307248, -268490, -294911, -291055, -337104, -302521, -266029, -244054, -253980, -307124, -339488, -335378, -343771, -262489, -302994, -327509, -325684, -322995, -280990, -341516, -355535, -285016, -272694, -298971, -333520, -308971, -282733, -262516, -274788, -298906, -333308, -303234, -325191, -303111, -294630, -286406, -284784, -278740, -264132, -324938, -278413, -315092, -280866, -279098, -331312, -309369, -305013, -324960, -339469, -278593, -282210, -270487, -282686, -341091, -331390, -286701, -284499, -341409, -315693, -345650, -307314, -288998, -280527, -300605, -309068, -313211, -320789, -278591, -304745, -304572, -254474, -291260, -324951, -325404, -306901, -283118, -287043, -290510, -290549, -310819, -296923, -303234, -287004, -286855, -297107, -297236, -302789, -314999, -274639, -290657, -268362, -262426, -290743, -325164, -268207, -282591, -288670, -266580, -292892, -246118, -298793, -303114, -258318, -242158, -262725, -281047, -335428, -311295, -292853, -280461, -288946, -282462, -248538, -284572, -313311, -272420, -319018, -247933, -252484, -244107, -294841, -327397, -345844, -274724, -246171, -250504, -333264, -274337, -280700, -292602, -254327, -290658, -298874, -276851, -292641, -320946, -291118, -276853, -274579, -219776, -294881, -301209, -293013, -262296, -233746, -276421, -310907, -288895, -290738, -294937, -316902, -303200, -270717, -317207, -287077, -306818, -335297, -250271, -254132, -286637, -248441, -264163, -304930, -329390, -339581, -343635, -288733, -274436, -284599, -339862, -327598, -329298, -295159, -278781, -294541, -306869, -310776, -303161, -370007, -276430, -302793, -288829, -315092, -327210, -315354, -321453, -264502, -286622, -292496, -333213, -276584, -315339, -262199, -290944, -287088, -343617, -312896, -335402, -296773, -308956, -325422, -282859, -339505, -284707, -319450, -329282, -250101, -266051, -381845, -284591, -327195, -268274, -335568, -315248, -272628, -260337, -284619, -274431, -284437, -320965, -251949, -276411, -298973, -278617, -309122, -351809, -325211, -296662, -288838, -317149, -296820, -298956, -308885, -257998, -288797, -274495, -238100, -329460, -317341, -341365, -316895, -310975, -262072, -288751, -307027, -304602, -333374, -272413, -274713, -300963, -288345, -242138, -329210, -284755, -249973, -280265, -282531, -264373, -278780, -292247, -258152, -325093, -294597, -249998, -253970, -247834, -278306, -294595, -260190, -227479, -253712, -258134, -268432, -278382, -278392, -235791, -243516, -213117, -260066, -264095, -251889, -270228, -262070, -259930, -247951, -251715, -255599, -249708, -255719, -276274, -249839, -268146, -241544, -260093, -231354, -280420, -223322, -259945, -235419, -284244, -257996, -296401, -266041, -257903, -247966, -243710, -282260, -272070, -239474, -262011, -262160, -249885, -239660, -251835, -265943, -251860, -264073, -245788, -249776, -235626, -257921, -274187, -286326, -233343, -241780, -253961, -229465, -219275, -269862, -263821, -255815, -288384, -197089, -257854, -264120, -241595, -270171, -255802, -235243, -215204, -241510, -235316, -253450, -245479, -266073, -199011, -268207, -202877, -213071, -239466, -231429, -222967, -214947, -192509, -208879, -228957, -215192, -235320, -237549, -210738, -204885, -245568, -249657, -229396, -221120, -214952, -212855, -202839, -229202, -182434, -210865, -227020, -188361, -227220, -235400, -202681, -216735, -200431, -231361, -241390, -225175, -178209, -208740, -235343, -217041, -226929, -202598, -186393, -216936, -204770, -221087, -233002, -192404, -192547, -198447, -229035, -204554, -190301, -223135, -223100, -174144, -169905, -198528, -176059, -208784, -210838, -196480, -190496, -196515, -200391, -218811, -214667, -255570, -186404, -202511, -204739, -222846, -214743, -184132, -153484, -186304, -229179, -194394, -216683, -171971, -226984, -159797, -200509, -174072, -190218, -184278, -198432, -184071, -196424, -198438, -198408, -184050, -184165, -200456, -186241, -190187, -169911, -182232, -190407, -175829, -184275, -178088, -163614, -194406, -182131, -139266, -182185, -196343, -185972, -183874, -190388, -153582, -184152, -182075, -165819, -182121, -188131, -159763, -171828, -175978, -149510, -151620, -194285, -145260, -175949, -180137, -173947, -198402, -171761, -141302, -184253, -182088, -153572, -182056, -153565, -143375, -125008, -131007, -159690, -155533, -149449, -125018, -157598, -167832, -135235, -139265, -155519, -137230, -151363, -145386, -108620, -127149, -165647, -143376, -110593, -145254, -139150, -121001, -131105, -127084, -124909, -128908, -110695, -100411, -108764, -149299, -125027, -112622, -118848, -110582, -120832, -98324, -116759, -102343, -137228, -126977, -106425, -102495, -94305, -124977, -116781, -82148, -116692, -96274, -96424, -104423, -104439, -73907, -98392, -116612, -118752, -110707, -128946, -98325, -82002, -104452, -118799, -108494, -83967, -79965, -96234, -108589, -80003, -86085, -82036, -110626, -141193, -108483, -96287, -94191, -114592, -96248, -102372, -90134, -100315, -88063, -90135, -81895, -112517, -92151, -69690, -104444, -104443, -94204, -86020, -102354, -96148, -114603, -88033, -83957, -88003, -83921, -77764, -77862, -86031, -85906, -98212, -94116, -83907, -110449, -94172, -81764, -96186, -94144, -71696, -85983, -63498, -71629, -100234, -102254, -85920, -90079, -87947, -94082, -104263, -100224, -94037, -85969, -73681, -67526, -73704, -86006, -71664, -75738, -69600, -81837, -75695, -87971, -79778, -77718, -75644, -77738, -81823, -100180, -83845, -67556, -51196, -73693, -61400, -63471, -67538, -73685, -59309, -55250, -81796, -75682, -63431, -67504, -67443, -73650, -55279, -55228, -47099, -49163, -57297, -55278, -22563, -59338, -61370, -65440, -32736, -51132, -53186, -51160, -36851, -36850, -34787, -32764, -40933, -30699, -43000, -28665, -47039, -16372, -34799, -44999, -45025, -24548, -26601, -32723, -26614, -34791, -18423, -18445, -20482, -14354, -16402, -12305, -18430, -20449, -18405, -22499, -28643, -22512, -18423, -10, -18417, -12285, -16386, -6148, 4064, -8202, -8196, -8187, -6141, -12277, -14314, -10231, -8184, -2045, -6149, -8189, -2048, -3, -2049, -2048, -6142, -9, -2052, 4086, -6144, -4094, -2047, -4097
```

```
Secret key: [1, 1, -1, 0, 1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, 0, -1, -1, 0, -1, -1, -1, 0, 0, 0, 0, 0, 1, -1, 0, -1, 0, 1, 1, 0, 0, 0, 0, 1, -1, 1, 1, 1, 1, 0, -1, 1, 0, 1, 0, -1, 0, -1, 1, -1, 0, 1, -1, -1, 1, -1, 1, 0, 0, -1, 1, 0, 0, 0, -1, -1, 1, 1, 0, -1, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, 1, 1, 1, 1, 0, 0, -1, 1, -1, -1, 0, -1, 1, -1, -1, 0, -1, 0, 0, 0, 1, 1, 1, -1, 0, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 0, 1, 0, 0, 0, 1, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, -1, -1, 1, 0, -1, 0, -1, -1, 0, 1, -1, -1, -1, 1, 1, 0, 1, 0, -1, 0, -1, 1, 0, 1, -1, 1, 0, 0, 1, 0, 0, 1, -1, -1, 1, 0, 0, -1, 0, 1, 1, 0, 0, 0, -1, -1, 1, 0, 1, -1, -1, 1, 0, -1, -1, 1, -1, 0, -1, -1, 0, 0, 0, -1, -1, 1, 1, 0, 1, -1, 1, 1, 1, 0, 0, 1, -1, 1, -1, 0, -1, 0, -1, 1, 0, -1, 1, 1, -1, 0, 0, 0, -1, 1, 1, 0, 1, 1, -1, 1, 0, 1, 1, 0, 1, 1, -1, -1, 0, 0, 0, 0, 1, 0, 0, -1, -1, -1, 0, -1, -1, -1, -1, 1, 1, 1, 0, -1, 0, -1, 0, 0, 0, 0, -1, -1, 0, 0, 1, 1, -1, 0, -1, 1, 1, 0, 0, 0, -1, 1, 0, -1, -1, 1, -1, -1, -1, 1, 0, -1, 0, 0, 0, 1, 1, -1, 1, 0, 0, 1, -1, 1, 1, -1, -1, 0, 0, 0, 0, -1, 0, 0, -1, 1, -1, 0, 1, -1, -1, -1, -1, 0, 0, 1, -1, 1, 1, -1, 0, -1, -1, 1, 0, -1, 0, -1, 1, 0, -1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 0, 1, 1, 0, 1, -1, 0, 1, -1, 1, -1, -1, 0, 0, 0, 1, -1, 0, -1, 1, 0, -1, 1, -1, 0, 0, 0, -1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, -1, 1, 1, 0, 0, 0, -1, -1, -1, 0, 0, 0, 1, 0, 0, 1, 1, -1, 0, 1, 0, 1, 1, -1, -1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, -1, -1, 1, 1, 0, -1, -1, 1, -1, 0, 0, 0, -1, -1, 1, 0, -1, 1, 1, 1, 0, 0, 0, 1, -1, -1, 0, -1, -1, -1, 1, -1, -1, 0, 0, -1, -1, -1, -1, 1, 0, -1, 0, 0, 0, -1, -1, 1, 0, -1, 1, 1, 0, -1, 1, 0, -1, -1, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 0, 0, -1, -1, -1]
```


