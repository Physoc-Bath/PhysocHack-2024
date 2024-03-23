import numpy as np
import matplotlib.pyplot as plt

#All the data on quasars split up into the individual columns
redShift = [0.7792, 0.6878, 0.6351, 2.6809, 3.0018, 2.287, 1.5738, 0.371, 1.1799, 2.2507, 2.5067, 1.5778, 3.085, 3.6972, 1.3024, 2.6678, 1.7998, 1.7363, 0.4044, 2.0688, 3.2217, 2.0913, 1.5913, 1.3713, 1.5626, 1.5395, 1.51, 1.5091, 1.4415, 1.2324, 1.831, 1.0573, 1.6256, 1.4647, 0.9664, 0.7993, 0.2894, 1.4368, 2.1019, 2.082, 1.1754, 3.1256, 0.8278, 1.4675, 1.1128, 0.5095, 0.6425, 0.6819, 2.1182, 1.9324, 1.1149, 1.4882, 1.6723, 2.5097, 1.8724, 1.9924, 1.3085, 3.7905, 1.0733, 1.985, 1.562, 0.4004, 0.8817, 2.855, 1.9296, 1.8442, 2.5754, 3.5741, 1.518, 3.422, 1.7353, 1.4657, 1.3452, 0.964, 2.3946, 1.0165, 0.8007, 1.5956, 0.9709, 1.5978, 1.1363, 2.1708, 1.4318, 0.5174, 1.5544, 1.472, 1.6733, 1.8126, 1.0601, 3.0591, 0.8084, 1.1575, 2.0473, 1.3221, 1.3897, 1.9496, 0.7423, 1.4329, 1.4244, 1.5268, 1.5123, 0.6214, 1.3352, 1.3465, 0.5702, 2.7216, 0.5778, 1.3574, 1.3932, 1.4158, 3.2588, 1.9464, 1.4723, 0.5923, 1.5379, 1.973, 0.8727, 2.1745, 0.93, 0.6871, 1.6299, 2.237, 3.146, 1.8457, 0.743, 3.0451, 0.4672, 2.5316, 1.0595, 2.3311, 3.359, 2.4499, 0.3546, 0.913, 0.2013, 0.8019, 0.6976, 1.1181, 1.6765, 1.1289, 1.7785, 1.0779, 2.8477, 0.551, 1.1343, 0.8055, 3.1604, 3.5596, 2.0834, 1.1785, 0.4062, 0.4947, 1.8975, 1.3419, 2.7574, 1.31, 0.8979, 2.134, 1.788, 1.8396, 1.8791, 1.8999, 1.7097, 1.2744, 1.8383, 1.5133, 1.2634, 2.4654, 1.8496, 3.4071, 2.1843, 1.04, 2.1298, 1.8124, 1.8735, 1.1258, 1.3899, 0.2856, 1.8306, 0.6122, 1.3113, 0.459, 1.5766, 1.3483, 0.3861, 2.581, 0.7038, 0.6333, 1.4897, 0.9262, 1.0126, 3.2769, 1.1114, 3.5267, 1.0236, 1.4181, 0.6344, 1.6129, 1.5668, 1.2774, 1.2953, 1.3461, 1.8286, 0.8147, 1.4725, 1.026, 0.9504, 2.0823, 1.2019, 0.6418, 0.7448, 2.9982, 2.1093, 2.9518, 0.967, 1.1151, 1.7599, 1.1133, 3.475, 0.9578, 1.6727, 0.726, 1.83, 0.813, 2.2904, 1.443, 0.7385, 1.8235, 1.861, 0.5487, 1.1368, 1.7907, 2.5973, 3.778, 0.4284, 3.738, 1.2919, 2.0234, 1.2228, 1.3223, 2.297, 0.4995, 0.8231, 0.9999, 0.9777, 2.1384, 3.4695, 1.6137, 2.1145, 1.1005, 1.015, 1.3546, 0.6065, 1.179, 1.514, 2.1996, 2.6484, 1.7244, 1.8014, 1.7985, 0.6071, 2.1871, 1.8935, 1.2272, 1.3435, 1.6107, 1.5595, 0.612, 3.8375, 0.8249, 2.5141, 1.2285, 2.2826, 2.5792, 3.1171, 0.4369, 1.1814, 0.4606, 2.0401, 1.7889, 1.1237, 1.232, 1.8644, 1.9443, 0.6013, 3.1593, 1.0247, 1.8385, 0.9342, 2.0985, 1.0562, 1.6292, 0.8077, 1.8861, 2.7236, 1.9718, 3.3334, 2.0131, 1.2166, 1.4062, 1.2194, 1.3079, 1.1333, 2.0114, 0.2408, 2.1239, 1.1545, 0.8813, 1.7997, 1.1251, 0.4859, 2.7727, 0.9372, 1.1111, 1.921, 1.2716, 1.3437, 1.6252, 1.3013, 0.3237, 1.568, 2.3281, 1.5377, 0.9144, 1.5828, 0.8199, 1.1353, 1.5719, 1.2872, 1.4136, 0.77, 0.5007, 1.3388, 1.4093, 1.5334, 2.6423, 1.1723, 1.9652, 0.3087, 1.7264, 0.2294, 0.8426, 0.5319, 0.7951, 1.4804, 1.7329, 0.8578, 0.494, 1.7647, 1.8593, 1.6792, 2.0349, 1.1488, 2.522, 0.7383, 2.9534, 1.9081, 1.1279, 2.1104, 0.5017, 2.9856, 0.2282, 1.4102, 0.6279, 2.1077, 1.6926, 1.6297, 4.4096, 1.3634, 2.0302, 1.0458, 0.6005, 2.6312, 2.7277, 1.8442, 3.6255, 1.055, 0.3485, 2.6941, 1.5667, 1.0516, 1.0702, 1.0145, 1.9643, 2.1013, 3.0254, 2.4152, 1.3046, 3.3303, 2.0712, 1.1973, 0.4082, 2.0445, 1.6244, 1.1503, 3.2491, 1.7358, 1.6471, 1.493, 0.6197, 2.5797, 2.4132, 1.4236, 2.559, 1.279, 1.9638, 1.1293, 0.4226, 0.3555, 1.5806, 0.5917, 1.5356, 1.488, 0.8605, 0.2812, 1.6762, 1.9173, 1.0924, 1.9236, 1.1759, 0.4221, 1.8372, 1.3966, 0.3964, 0.5354, 3.6594, 4.8099, 2.6852, 2.1302, 0.2158, 1.0284, 1.2057, 1.4554, 0.9107, 1.365, 1.9683, 1.213, 0.8347, 1.4404, 1.4184, 1.9272, 1.3527, 1.3294, 0.5998, 0.7413, 1.1981, 0.8288, 1.448, 3.6686, 3.1502, 1.3045, 3.1512, 1.2879, 0.366, 1.8396, 1.9181, 1.7724, 2.2439, 1.5117, 0.7138, 0.6807, 1.955, 1.8713, 0.5404, 2.3892, 2.0566, 2.8087, 0.4412, 3.2284, 1.5131, 1.783, 1.7592, 1.7705, 1.5087, 1.6034, 1.2133, 4.0271, 0.6313, 0.4515, 1.6646, 1.7756, 1.6698, 1.4775, 1.8123, 1.1001, 1.8482, 1.7647, 1.6819, 1.6063, 1.7644, 0.5762, 1.5378, 1.4537, 1.524, 1.4972, 0.9733, 4.8063, 1.2975, 1.7869, 1.7483, 2.039, 2.3907, 1.4122, 1.2131, 1.3563, 1.2977, 0.5603, 0.451, 2.7814, 1.8838, 0.73, 1.3398, 0.8913, 2.3904, 3.2021, 1.8167, 0.5769, 1.3539, 0.7838, 2.1376, 3.352, 0.3045, 1.7364, 1.2562, 1.6645, 0.6458, 3.2461, 0.946, 0.8159, 1.8478, 1.8478, 0.7306, 2.1152, 0.9401, 1.6595, 1.8281, 1.4501, 0.7603, 2.4923, 1.4918, 3.45, 1.4047, 1.7099, 2.2865, 1.2482, 1.1576, 2.0853, 1.5862, 1.3856, 1.7246, 0.3472, 2.109, 1.5395, 0.7674, 1.1262, 1.0487, 2.714, 2.995, 3.0769, 1.1112, 1.3914, 1.0428, 1.1214, 0.6333, 1.8182, 2.3007, 1.1143, 1.1541, 3.871, 1.506, 0.582, 1.8506, 0.9983, 1.7541, 3.4942, 0.5112, 1.9212, 1.2046, 1.0518, 1.5487, 1.4146, 0.8803, 1.1294, 1.862, 1.2752, 1.0004, 2.1581, 0.623, 0.6241, 1.6802, 0.3274, 1.3776, 1.1912, 1.6197, 0.541, 1.8683, 2.1855, 1.5602, 1.5018, 1.9072, 1.4172, 3.5399, 3.0268, 3.0117, 0.7782, 0.2293, 2.0858, 1.6672, 1.6298, 0.6384, 1.1902, 1.6991, 0.9994, 0.8294, 1.6769, 0.8692, 0.5594, 1.3608, 1.3532, 1.5152, 2.6879, 2.964, 0.5657, 1.0474, 1.5372, 0.4385, 0.7783, 1.8589, 2.111, 1.5541, 1.6813, 1.4789, 1.4894, 0.6324, 1.88, 1.298, 1.6384, 0.3565, 2.0184, 1.6093, 1.7667, 1.4883, 1.7934, 0.5553, 0.8243, 1.9226, 1.3404, 0.2432, 2.06, 1.7792, 1.7172, 1.1795, 0.7734, 0.9865, 0.9668, 2.0259, 1.5078, 1.8473, 3.3238, 0.938, 1.8016, 2.4097, 4.154, 0.1544, 1.995, 1.6123, 1.2009, 2.4318, 1.4626, 1.7909, 1.4702, 0.5662, 0.7227, 0.8306, 1.8667, 1.9357, 0.8939, 1.4387, 1.3309, 3.0377, 0.2556, 1.7242, 1.1699, 1.0144, 0.6416, 2.3425, 2.0456, 0.3846, 1.9521, 2.3878, 1.4525, 4.3087, 0.2276, 1.4324, 1.661, 2.0808, 1.3375, 1.3124, 1.6865, 0.7373, 3.1824, 1.407, 1.5942, 1.428, 1.5937, 0.6318, 3.3035, 0.8849, 2.7575, 0.6231, 0.7589, 0.5796, 2.7112, 2.1554, 1.9058, 0.9735, 1.7332, 1.8778, 0.3969, 1.5295, 0.6973, 1.2312, 1.9479, 1.2796, 0.6524, 1.8193, 1.1457, 0.8145, 1.9575, 2.1496, 1.1801, 3.0919, 0.8849, 1.3084, 0.5606, 0.6485, 1.6182, 2.1778, 0.7516, 1.2568, 1.7255, 0.5204, 1.1922, 0.3218, 1.2141, 1.4904, 1.0271, 1.4721, 0.4078, 1.9583, 0.3384, 0.6569, 0.7623, 2.1999, 1.9644, 1.0241, 1.8559, 0.9605, 1.7773, 0.9088, 1.9184, 3.6719, 0.4006, 1.4058, 0.5641, 1.1982, 3.0064, 1.868, 1.7234, 1.4813, 2.2345, 3.2024, 0.7919, 1.9474, 0.6101, 1.3601, 3.1763, 1.1898, 0.9921, 0.7198, 1.7611, 0.8087, 1.2341, 1.4941, 1.6018, 0.8102, 0.9189, 2.5416, 1.7595, 1.9033, 1.2957, 1.1487, 0.5358, 1.9423, 1.06, 2.2798, 0.8485, 2.2677, 1.569, 1.7415, 1.6032, 2.0023, 1.8034, 1.0751, 1.3279, 2.4474, 1.1391, 0.6446, 1.4491, 2.3228, 1.0901, 0.8224, 3.6753, 1.5062, 0.3877, 1.2282, 1.1083, 1.0634, 1.235, 0.2093, 1.086, 0.1685, 0.838, 1.2126, 1.253, 2.0513, 1.3743, 1.988, 0.7704, 1.6902, 1.2172, 1.8786, 2.2142, 2.1529, 0.4233, 1.1156, 1.0458, 2.138, 0.8981, 1.3018, 1.5535, 0.3247, 1.6717, 4.7174, 1.4373, 1.8144, 3.0063, 1.3116, 1.0609, 2.1748, 2.3226, 2.1514, 1.5457, 1.1128, 1.4238, 1.5861, 2.7799, 2.2051, 2.3438, 0.4436, 2.1741, 2.1572, 1.9886, 3.0784, 1.9591, 1.2195, 1.7606, 0.5814, 1.4579, 1.1557, 1.9068, 1.4242, 1.0015, 1.9948, 1.1726, 1.4231, 0.7788, 1.6857, 1.3802, 0.4551, 1.2032, 3.585, 1.4511, 1.7609, 1.6491, 0.6692, 1.6873, 1.3803, 1.3958, 1.7997, 0.8565, 0.7785, 3.6824, 1.0279, 0.6657, 1.2382, 0.36, 0.6069, 1.2214, 1.7115, 1.2217, 1.7129, 2.5145, 2.094, 2.3026, 1.21, 0.5735, 1.1697, 1.6494, 1.6325, 1.8678, 1.2556, 1.249, 1.657, 1.3134, 1.4818, 0.9985, 2.8971, 2.125, 1.472, 1.7476, 1.5725, 1.5052, 1.0468, 1.6795, 1.75, 1.037, 1.4418, 1.9473, 0.9606, 1.5605, 1.1204, 1.4817, 0.6615, 1.3628, 1.7376, 0.6276, 2.2318, 1.0841, 1.3589, 1.5644, 1.2457, 1.3611, 0.3115, 1.4216, 2.1137, 1.23, 1.1017, 1.3184, 2.3346, 1.9598, 1.7827, 1.9203, 0.3876, 1.828, 2.0908, 2.5866, 0.8886, 1.4324, 1.5555, 2.6653, 1.7382, 1.1349, 0.5691, 1.9204, 2.8764, 1.5326, 2.4084, 0.2656, 1.6261, 1.1903, 1.8023, 0.4081, 4.0108, 1.1346, 2.0942, 2.317, 1.5526, 2.3123, 1.8336, 3.8545, 0.9392, 0.2647, 2.3656, 1.039, 1.129, 0.3504, 1.7746, 1.6839, 1.5703, 1.782, 1.2137, 0.8054, 1.9495, 1.5042, 1.5273, 0.4996, 4.3296, 0.789, 1.3206]
bhmass = [9.24594, 8.14573, 8.6235, 9.06812, 9.15732, 10.005, 9.22076, 9.42531, 8.55337, 9.10631, 9.44334, 9.16526, 9.15245, 9.83215, 8.8656, 9.12349, 9.40747, 8.52565, 8.18102, 8.9442, 8.68755, 8.9656, 9.17902, 9.03196, 9.24538, 9.70199, 9.26667, 9.59135, 9.03876, 8.99918, 8.57168, 8.65177, 8.7449, 8.9193, 9.206, 8.96128, 9.18484, 9.14632, 9.60378, 8.17089, 9.66808, 10.0405, 7.67801, 8.83638, 8.66026, 8.55407, 8.80447, 8.67811, 9.41515, 9.81723, 9.42029, 8.97062, 8.68774, 10.5948, 9.15071, 9.41835, 9.28959, 9.85699, 9.13238, 9.20101, 8.67227, 8.6256, 9.03696, 9.54513, 9.904, 8.56695, 8.11303, 8.92877, 9.03341, 9.24029, 8.48853, 9.41921, 9.24086, 8.98309, 8.68441, 8.38839, 8.33222, 8.13076, 9.32427, 9.13366, 8.84699, 8.85227, 9.26857, 7.36896, 8.9158, 9.14974, 9.0464, 9.163, 9.19521, 8.23587, 9.19179, 8.56617, 9.24529, 9.01229, 8.97736, 8.8982, 8.73536, 9.58131, 8.72096, 9.26256, 9.78079, 8.93713, 8.70577, 9.29936, 8.22005, 8.71279, 9.37979, 8.78831, 8.78989, 8.60875, 9.52761, 8.80749, 9.02035, 8.44858, 9.26441, 9.73707, 8.0654, 9.87276, 8.75894, 8.86436, 9.17101, 8.37851, 9.91838, 9.11665, 8.75674, 8.90887, 7.9469, 9.50965, 9.18547, 8.76805, 8.52745, 9.41678, 7.84495, 8.98388, 8.7473, 8.72916, 9.09733, 8.73468, 9.50027, 8.67121, 8.66911, 7.95907, 9.05148, 7.88356, 8.58966, 8.39949, 9.20006, 9.32493, 9.33395, 8.80647, 8.51576, 8.3707, 9.16934, 9.16621, 9.83748, 8.79453, 8.96227, 8.34399, 8.71229, 8.89535, 8.12209, 8.68963, 9.03893, 8.71598, 9.90814, 8.93828, 9.14475, 9.03587, 9.01202, 9.6526, 9.14105, 8.77786, 9.58349, 9.6284, 9.47921, 8.82944, 9.37173, 7.89276, 8.71609, 8.45824, 8.52971, 7.99833, 9.15367, 9.02705, 8.27501, 9.51454, 8.44821, 8.01601, 9.61539, 8.82598, 8.87253, 9.62135, 9.8734, 9.28109, 8.25509, 8.63933, 8.31693, 9.32551, 9.01887, 8.98295, 8.66665, 8.1265, 9.61283, 8.91132, 9.29174, 9.06651, 8.77575, 9.7885, 9.31616, 8.69293, 9.4404, 9.59738, 9.63474, 9.37744, 9.47655, 9.4762, 8.87449, 8.91628, 9.36718, 8.79398, 9.70259, 8.78876, 9.19481, 8.71193, 9.42683, 9.00027, 9.02834, 9.40943, 9.46121, 8.49765, 9.28373, 9.45048, 8.36747, 9.36742, 8.55654, 8.63204, 8.97296, 8.52574, 9.36029, 8.55486, 9.13914, 8.53317, 8.5595, 8.45206, 8.70758, 8.96185, 9.96535, 9.18603, 8.8598, 9.34312, 8.69921, 8.97409, 8.09591, 8.15509, 8.56761, 9.26564, 8.93272, 9.28443, 7.85592, 9.53025, 9.08426, 9.1713, 8.10233, 8.95369, 8.73089, 8.87119, 9.0737, 9.43682, 9.71476, 8.38446, 8.86389, 9.04187, 9.05216, 8.33195, 9.347, 7.77503, 9.18458, 9.00641, 9.12768, 9.40669, 9.06117, 9.16903, 9.04975, 9.78302, 7.16997, 8.51664, 8.87432, 9.15827, 9.20741, 9.20433, 8.6546, 9.2089, 8.58118, 9.14199, 8.679, 9.37835, 9.96095, 8.97271, 7.80958, 9.20647, 8.82764, 9.14728, 8.84118, 9.25496, 8.19307, 9.76413, 8.94262, 8.82731, 9.40292, 9.13698, 7.97013, 9.37908, 8.60479, 8.50834, 9.17113, 8.64309, 9.21983, 9.16289, 9.28308, 8.54993, 8.65778, 9.86353, 8.9663, 8.46412, 9.14356, 9.1073, 8.97088, 8.54778, 9.4242, 8.75854, 8.58229, 8.58283, 8.60287, 8.83534, 9.11542, 9.58942, 8.98402, 9.05483, 7.21091, 9.5629, 8.00234, 8.91378, 9.71142, 8.42414, 9.6694, 9.29263, 8.76043, 9.4148, 9.35198, 8.85073, 8.98098, 8.84369, 9.41934, 9.09734, 8.68019, 9.27174, 8.97322, 9.03566, 9.18564, 8.45567, 7.88805, 8.66216, 9.26757, 8.19373, 8.22916, 9.67617, 9.32527, 9.50241, 8.30197, 8.54023, 9.1764, 8.55994, 9.89017, 9.79218, 8.569, 9.16019, 8.46784, 8.74377, 9.42578, 8.60545, 8.71955, 9.28771, 9.04956, 8.72144, 9.45843, 9.30208, 8.8242, 9.31118, 8.90634, 8.67098, 8.76059, 8.16202, 9.16722, 9.00607, 8.65385, 9.24447, 9.26848, 9.03656, 8.9958, 8.25311, 9.84182, 8.95999, 8.56566, 8.88602, 9.37739, 8.98306, 8.57543, 7.89822, 8.34936, 9.60131, 8.46484, 9.79047, 9.77784, 10.1566, 7.82061, 8.54134, 8.82602, 9.40317, 8.9081, 8.29856, 9.26003, 9.16185, 8.99852, 9.05209, 8.68255, 8.53774, 8.49065, 9.45011, 9.39621, 8.58833, 8.54811, 8.91322, 9.53735, 9.10338, 9.055, 8.99412, 8.76675, 8.84879, 8.53913, 9.92239, 8.58139, 9.01267, 8.53406, 7.92261, 8.68393, 9.05915, 8.84154, 9.05937, 8.40504, 9.63125, 8.90789, 9.24942, 8.94883, 8.27155, 9.63423, 8.71767, 9.69005, 9.47252, 9.24143, 8.83367, 8.17269, 9.12339, 9.17627, 7.80343, 9.69262, 9.3473, 9.26564, 7.93058, 9.13551, 8.98861, 8.40934, 9.08672, 9.55212, 9.30143, 8.73826, 9.51457, 8.78524, 8.16916, 8.64387, 9.01117, 9.48813, 9.2828, 9.158, 9.40127, 9.02491, 8.35301, 8.32459, 9.16753, 9.09617, 9.69421, 8.63521, 8.5464, 8.4298, 9.35948, 8.88792, 8.75026, 9.29365, 9.26233, 9.3116, 8.41002, 7.78823, 9.7138, 9.13826, 8.72367, 9.43422, 8.95832, 8.6703, 8.45206, 9.33155, 9.45033, 8.8938, 8.93953, 8.80287, 9.64941, 8.05654, 9.13079, 9.10375, 8.90791, 9.2174, 7.97061, 8.3357, 8.01799, 9.15657, 9.37598, 8.89852, 8.43553, 9.08395, 9.33996, 8.59375, 9.20032, 8.76685, 8.77028, 9.8436, 8.90851, 9.87191, 9.63063, 9.33721, 8.43651, 9.49389, 9.01496, 9.5833, 8.83308, 8.55447, 8.73034, 8.91102, 8.79226, 9.61315, 8.58992, 8.86654, 8.05173, 10.0636, 9.27902, 9.19949, 7.82978, 9.20234, 8.11072, 9.50141, 8.17155, 9.59596, 8.25015, 9.31198, 9.33138, 9.34242, 9.32443, 8.99777, 8.73767, 8.8894, 8.28919, 9.41982, 8.86067, 9.53637, 8.88766, 9.25669, 8.76474, 9.54152, 8.53708, 9.457, 9.40641, 9.30099, 9.05727, 9.25251, 8.61588, 9.0593, 9.19213, 8.7937, 9.58279, 8.72195, 8.03678, 8.70196, 8.14483, 8.43171, 8.8098, 8.61771, 9.06962, 9.06944, 9.34113, 9.59928, 8.95206, 9.57598, 9.31392, 9.10681, 9.20055, 9.09508, 9.16784, 9.21151, 8.44675, 9.06361, 9.07565, 8.99837, 8.39426, 8.90343, 9.32612, 8.69671, 8.57724, 9.05708, 8.66465, 8.99647, 8.94644, 8.87351, 9.50589, 8.43209, 9.23454, 8.45941, 9.11581, 9.26891, 7.95141, 9.03937, 9.32229, 9.34252, 8.83593, 9.07232, 9.08957, 8.91559, 8.03636, 9.6265, 8.82335, 8.75499, 8.46691, 9.36059, 8.94341, 8.28434, 9.04018, 8.76491, 7.84316, 8.54821, 9.18037, 9.59719, 8.27865, 8.93777, 9.52802, 8.95848, 8.96803, 8.49988, 9.24937, 9.03145, 9.76156, 9.12771, 9.13193, 8.62077, 8.53548, 9.01807, 9.40159, 10.493, 7.99196, 8.79876, 9.97185, 9.38291, 9.48132, 9.25356, 8.90242, 8.68765, 8.70919, 10.189, 8.71254, 9.37604, 8.94399, 8.74746, 9.19168, 9.6235, 9.1404, 8.33128, 9.72383, 9.1277, 9.17397, 8.76238, 9.53554, 9.33478, 8.07757, 8.79237, 8.29864, 9.43495, 8.51693, 8.57249, 9.01604, 8.50317, 8.60436, 9.1209, 8.97606, 8.89174, 8.60962, 9.29797, 8.85819, 8.45418, 8.68071, 8.97785, 9.1, 8.17845, 8.06446, 8.59581, 8.45457, 8.15772, 8.96155, 10.1693, 9.7011, 8.62186, 8.85701, 8.83629, 9.39342, 8.72192, 9.04004, 8.47665, 8.90796, 8.54719, 8.83161, 8.76509, 8.98618, 8.97198, 8.77997, 9.0682, 8.95245, 9.05171, 9.5976, 8.90605, 8.20875, 7.93307, 8.15094, 9.61255, 9.53746, 8.17821, 8.78248, 9.15518, 8.63446, 9.18005, 8.61444, 8.98533, 8.78156, 8.62271, 8.95118, 8.41036, 8.50189, 8.38876, 9.31173, 8.53456, 9.05901, 8.36635, 8.0885, 9.29473, 8.83553, 9.08088, 8.66623, 9.03936, 9.40084, 9.00405, 9.30901, 9.21688, 8.36565, 8.15245, 9.33446, 8.81146, 8.94207, 9.26655, 9.854, 8.42496, 9.67405, 8.46865, 8.58689, 10.0333, 8.61949, 8.58055, 8.42162, 8.68974, 8.44678, 9.25999, 8.98919, 9.34928, 8.39735, 8.45631, 8.21041, 9.56832, 8.48721, 9.78186, 8.9173, 7.87327, 8.74488, 8.66162, 9.52604, 8.84883, 8.60195, 8.0913, 9.37172, 9.024, 9.53886, 9.29337, 8.61015, 8.2382, 8.84605, 8.78837, 8.76871, 8.43394, 9.09165, 8.01273, 8.72468, 9.25945, 8.7128, 7.93706, 9.36296, 8.99029, 8.55988, 9.11943, 8.5279, 8.25242, 8.35682, 9.07495, 9.10147, 9.11094, 10.2392, 8.93874, 9.85814, 8.12842, 9.39228, 9.08361, 9.4219, 8.81345, 9.16406, 8.77017, 9.21516, 8.94234, 9.28878, 7.9467, 9.19831, 9.40743, 8.00098, 8.79322, 9.59031, 8.99013, 9.38547, 9.57489, 8.4315, 8.59068, 9.08413, 9.07573, 9.12609, 9.32355, 8.79257, 9.21928, 9.14846, 9.63127, 9.78745, 9.00128, 8.76066, 9.31798, 8.21626, 9.35967, 9.46677, 9.36719, 8.68215, 9.32514, 8.98978, 8.71656, 8.82583, 9.46647, 8.63309, 8.71497, 9.17079, 9.3668, 9.00145, 8.59364, 8.80245, 8.79939, 8.12068, 8.80734, 8.81744, 9.0104, 8.86257, 8.78507, 8.56816, 9.55052, 9.44828, 9.26883, 9.33038, 8.56364, 8.71543, 8.50459, 8.48172, 8.82243, 8.85522, 7.42169, 7.6407, 9.01274, 9.15957, 9.0824, 8.96995, 9.38673, 8.16619, 9.45176, 8.69063, 8.2753, 8.80927, 8.48809, 8.74004, 9.07921, 8.3644, 9.05476, 9.02314, 9.65828, 9.26742, 8.96067, 8.71581, 9.55273, 9.23455, 10.1362, 9.35753, 8.81928, 8.49164, 8.91259, 9.35639, 8.63689, 9.1399, 8.72079, 7.85741, 9.41609, 9.04886, 9.1206, 8.78243, 8.87333, 9.19923, 8.68415, 9.01846, 8.62949, 8.70895, 8.71529, 9.05176, 8.94563, 8.81413, 9.63936, 9.1745, 9.06104, 9.07724, 9.37115, 9.0818, 9.83692, 9.61067, 8.76305, 7.93501, 9.3546, 8.72583, 9.67323, 9.32577, 8.96987, 9.11633, 8.81351, 9.43048, 9.23774, 8.41217, 9.03449, 9.26969, 8.93549, 8.83276, 8.57111, 8.9424, 8.94794, 9.02695, 7.83144, 9.06514, 9.04359, 9.51644, 9.12484, 9.19201, 9.47846, 8.81303, 9.77721, 9.43447, 7.97817, 8.56926, 8.27007, 9.6635, 8.15911, 9.23079, 9.07345, 8.62815, 9.298, 8.94842, 8.95793, 8.72659, 9.0137, 8.83163, 8.36757, 9.30594, 8.88848, 8.74729]
lum = [39.494, 38.4911, 38.4543, 40.0064, 40.0422, 40.2462, 39.476, 38.3554, 38.7689, 39.5552, 39.9951, 39.5277, 39.7945, 39.6003, 38.9531, 39.5858, 39.5036, 38.3329, 38.3842, 39.8068, 39.6614, 39.6978, 39.5459, 39.0925, 38.9496, 39.6268, 39.5097, 39.2876, 39.0847, 39.1866, 38.5121, 39.0373, 39.537, 39.4323, 39.5181, 38.9565, 38.1936, 39.2592, 40.4554, 39.2273, 39.3461, 40.7004, 38.6009, 39.4653, 39.3084, 38.4896, 39.4275, 38.3126, 39.6126, 40.0755, 39.9031, 39.6503, 39.1113, 40.3392, 39.1308, 39.7955, 39.4577, 40.2567, 39.4951, 39.637, 38.9571, 38.3942, 39.3317, 39.6084, 40.3347, 39.1065, 39.3417, 39.8691, 39.2374, 39.7644, 39.6213, 38.9547, 39.3681, 39.1553, 39.9327, 39.2707, 38.2992, 38.7999, 39.7014, 39.3302, 38.8166, 39.5595, 39.3487, 37.8771, 39.4423, 39.0174, 39.5039, 39.6354, 39.661, 40.0058, 38.9364, 39.0733, 39.9195, 39.3415, 39.2181, 39.7181, 38.5477, 39.5008, 39.4128, 39.4833, 40.1932, 38.8806, 39.0193, 39.5706, 38.6092, 39.9681, 38.1083, 39.2317, 39.3387, 39.0225, 40.0092, 39.1017, 39.4448, 38.7409, 39.7124, 40.0385, 39.1371, 40.0553, 39.1214, 38.9889, 39.5887, 38.9725, 40.9421, 39.269, 38.8131, 39.7587, 37.9592, 39.9771, 39.2822, 39.3089, 39.5132, 40.0293, 38.4325, 38.577, 38.1009, 38.8524, 39.0893, 39.2942, 39.5453, 39.3201, 39.5314, 39.3232, 40.1431, 38.192, 38.7542, 38.8689, 39.6571, 39.8963, 40.1657, 39.2361, 38.3023, 38.59, 39.5134, 39.3187, 40.2193, 39.057, 39.0429, 39.2777, 39.2318, 39.4384, 39.3351, 39.2174, 39.7384, 38.7603, 39.956, 38.8753, 38.9284, 39.8334, 39.5503, 40.3447, 39.8303, 38.9859, 39.6278, 39.7896, 39.5773, 39.1613, 40.1289, 38.8704, 39.5035, 38.2698, 39.0116, 38.9182, 39.4224, 39.4201, 38.2936, 39.8948, 38.9133, 38.6717, 38.9064, 39.1529, 39.0048, 39.9338, 39.8185, 39.9383, 38.7921, 38.9695, 38.7488, 39.5477, 39.4554, 38.8376, 39.0008, 38.7993, 39.6385, 38.489, 39.7368, 38.7779, 38.7398, 39.9497, 39.7489, 38.6532, 38.9926, 40.256, 40.2273, 39.856, 39.5544, 39.8337, 39.5647, 39.316, 39.7579, 39.2714, 39.3545, 38.716, 39.7797, 38.5251, 40.0764, 39.621, 38.5309, 39.7112, 40.2027, 38.7622, 38.7353, 39.6279, 39.447, 40.2926, 38.1085, 40.0153, 39.2243, 39.5463, 39.691, 39.293, 39.9053, 38.613, 38.5027, 38.925, 39.1019, 39.3762, 40.0862, 39.0976, 39.1877, 39.2958, 38.936, 38.8815, 38.3789, 38.7202, 39.4626, 39.9476, 39.4149, 39.5108, 38.4198, 39.3652, 38.6039, 39.319, 38.7953, 39.2722, 38.8343, 39.5761, 39.4711, 38.7105, 40.0823, 38.5588, 39.399, 38.7661, 39.3983, 39.4873, 40.0472, 38.2057, 39.1264, 38.7414, 39.9769, 39.3438, 39.0758, 39.4521, 39.9168, 39.858, 38.1677, 39.6281, 39.2667, 39.606, 39.2103, 39.8231, 39.1788, 39.4561, 39.3045, 39.2285, 39.5364, 39.8136, 40.5313, 39.7618, 38.8182, 39.399, 38.6438, 39.4352, 39.2364, 39.9577, 38.0319, 39.9509, 39.3638, 38.8231, 39.1454, 39.6975, 38.6049, 40.0291, 38.9181, 38.8612, 39.8678, 39.2069, 39.5771, 39.4734, 39.5319, 38.1667, 39.4368, 40.0865, 39.3655, 39.0408, 39.0888, 39.2287, 39.324, 39.4216, 39.5805, 39.0295, 38.9612, 38.4452, 38.4916, 39.3858, 39.727, 39.8789, 39.2073, 39.6798, 38.2267, 39.7924, 38.277, 39.0679, 38.6692, 38.855, 39.1588, 39.8344, 38.8042, 39.2318, 39.1292, 39.7644, 39.42, 39.5384, 39.5121, 39.9693, 38.8884, 40.0616, 39.6688, 39.3462, 40.1221, 38.8752, 39.2693, 38.3799, 39.5473, 38.4826, 39.5599, 39.788, 39.727, 39.9288, 39.2613, 39.8529, 38.9297, 38.4643, 40.499, 39.3825, 39.3902, 39.7891, 38.6783, 38.287, 39.4897, 39.6611, 38.988, 39.0335, 39.366, 39.0636, 39.8773, 40.0757, 39.1194, 38.6818, 39.6232, 39.6556, 39.2385, 38.3918, 39.7228, 39.4551, 39.1003, 39.7273, 39.5937, 39.5467, 39.5214, 39.0203, 40.3046, 39.9581, 39.2319, 39.7602, 39.6867, 39.7328, 38.9192, 38.5205, 38.2575, 39.9556, 38.7032, 39.6122, 39.2563, 38.9154, 38.1602, 39.3929, 39.2496, 39.7069, 39.4095, 39.2296, 39.2653, 39.5661, 39.5213, 38.9013, 38.1898, 39.591, 40.0579, 40.0031, 39.755, 38.1633, 38.9904, 39.4854, 39.8686, 39.404, 39.2332, 39.6835, 38.5582, 39.255, 38.8152, 40.471, 39.4276, 39.5236, 39.2165, 38.3931, 38.8892, 39.2135, 39.5345, 39.2466, 39.8748, 40.4858, 39.1875, 39.8002, 39.0202, 38.1686, 39.6991, 39.6509, 39.9973, 39.5914, 39.7257, 38.7448, 38.0281, 38.4304, 39.6686, 38.7133, 39.5699, 39.9025, 40.3068, 37.9951, 39.3755, 39.4567, 39.8868, 39.0937, 39.5571, 39.1715, 39.2783, 40.0341, 39.9902, 38.2888, 38.5254, 39.4631, 40.0945, 39.7631, 39.7363, 39.1641, 39.1649, 39.3069, 39.0042, 39.5589, 39.4385, 39.587, 38.5461, 39.3548, 39.1444, 39.7343, 39.221, 39.2724, 40.0238, 39.3985, 39.5165, 39.208, 38.868, 39.9791, 39.1001, 39.2208, 39.5401, 39.1725, 38.8065, 38.668, 39.5595, 39.647, 38.7426, 39.398, 38.5443, 40.092, 39.8858, 39.5081, 39.0201, 39.5726, 38.7849, 39.1066, 39.7408, 38.2187, 39.3291, 38.9218, 38.9049, 38.7478, 39.7238, 38.5689, 38.612, 39.3949, 39.1564, 38.7005, 39.954, 39.0867, 39.6408, 39.6378, 39.7525, 38.8654, 39.8842, 39.4041, 40.0741, 38.8159, 39.2463, 40.0036, 39.7654, 39.154, 39.5906, 38.8716, 39.4693, 38.3103, 38.0827, 39.8472, 39.46, 38.7791, 39.711, 38.2666, 39.9267, 39.2295, 39.9968, 39.0476, 39.8282, 39.3818, 39.5076, 38.3859, 39.1858, 39.8569, 39.9081, 39.2776, 40.49, 39.5564, 38.8146, 39.2906, 39.2582, 39.0547, 39.8525, 38.1952, 39.221, 39.2141, 39.7037, 39.2742, 39.6685, 39.217, 39.2569, 39.6344, 39.2526, 39.1569, 39.0616, 38.6988, 38.6457, 39.4377, 38.551, 38.5283, 39.2138, 39.4356, 38.9317, 39.6103, 40.1221, 38.9283, 39.7085, 39.7543, 39.566, 39.6735, 39.6349, 39.8457, 39.3775, 38.266, 39.8268, 39.2731, 39.6571, 38.2935, 39.2986, 39.5223, 39.4135, 39.0417, 39.5052, 39.048, 39.1044, 38.7676, 39.157, 39.6035, 39.7477, 40.032, 38.5121, 39.5695, 39.0701, 38.6436, 38.8837, 39.962, 39.6239, 39.2055, 38.9229, 39.7269, 39.6291, 38.8183, 39.6784, 39.4283, 39.4828, 38.7428, 39.9915, 39.4238, 39.6304, 39.3212, 39.0816, 37.7986, 39.2917, 39.3222, 39.063, 38.0222, 39.6861, 39.1363, 38.7793, 39.1458, 38.746, 39.2248, 38.9876, 39.9807, 39.0175, 39.6587, 39.7903, 39.1226, 39.9046, 38.9611, 39.97, 38.0884, 39.1117, 39.7996, 39.1732, 39.9591, 39.7681, 39.2973, 39.0005, 38.2909, 38.2819, 38.8002, 39.65, 39.0669, 38.5819, 39.8821, 39.3882, 39.2578, 38.4636, 40.0144, 39.8207, 39.5762, 39.744, 39.8756, 39.5381, 38.3222, 39.6559, 39.1991, 39.3177, 40.0844, 38.5233, 39.5277, 39.1908, 39.1624, 39.4289, 39.3033, 39.5192, 38.4062, 39.8788, 38.9983, 39.1904, 39.2718, 39.4478, 39.1926, 39.1918, 38.8556, 39.4526, 38.7621, 38.3165, 38.6609, 40.2707, 40.0563, 39.5667, 39.1141, 39.4989, 39.2732, 38.8605, 39.7029, 38.4599, 39.4227, 39.6731, 39.3235, 38.7858, 39.3, 39.296, 38.8407, 39.0031, 39.8172, 39.2841, 40.0651, 39.2766, 38.935, 38.1306, 38.7675, 39.4193, 40.2421, 39.0303, 39.308, 39.688, 38.6927, 39.2454, 38.2969, 39.0496, 39.5799, 38.709, 39.1398, 38.3576, 39.7206, 38.4529, 38.7725, 38.7493, 39.7792, 38.8142, 39.1287, 39.6922, 39.1951, 39.6284, 38.5804, 39.2583, 40.0571, 38.3503, 39.4146, 38.6697, 39.2117, 39.5804, 39.75, 39.0127, 39.4106, 39.956, 40.1764, 38.8565, 39.7352, 38.6738, 39.4172, 40.0699, 39.1564, 38.786, 38.9147, 39.2928, 38.9199, 39.2312, 39.3488, 39.6999, 38.8002, 39.0801, 39.4959, 39.6608, 38.2603, 39.3835, 39.1958, 38.4442, 39.7112, 39.2864, 40.1721, 38.5446, 39.56, 39.2321, 39.3843, 38.8645, 39.3916, 39.3395, 38.977, 39.079, 39.2511, 39.2472, 38.7832, 39.1309, 39.5037, 38.8427, 38.8345, 39.8207, 38.8704, 38.1576, 39.5687, 39.102, 38.6239, 39.2076, 38.1378, 38.8474, 38.0474, 39.5425, 39.4338, 38.779, 40.0161, 39.4546, 40.0986, 38.3703, 39.729, 39.2774, 40.0044, 39.6881, 39.8696, 38.5259, 38.9872, 39.3996, 39.2022, 38.8331, 39.4486, 39.3805, 38.1917, 39.6665, 40.0227, 39.4868, 39.3826, 39.947, 39.2921, 38.7524, 39.5786, 39.9065, 39.4725, 39.2797, 39.3483, 39.7713, 39.4673, 39.6082, 38.943, 39.54, 39.0703, 39.8609, 39.2444, 39.6763, 39.4983, 39.7656, 38.5964, 39.8301, 38.8872, 38.9004, 38.5376, 39.8424, 39.71, 39.0733, 39.7887, 38.8034, 39.3551, 38.7881, 38.9888, 39.3056, 38.3746, 39.2648, 39.793, 39.3679, 39.8816, 39.6387, 39.1939, 39.1016, 39.0677, 39.4089, 39.8618, 38.3765, 38.5161, 39.5925, 38.5248, 38.809, 39.4552, 38.2318, 38.5783, 39.3241, 39.5524, 39.5237, 38.9268, 39.3395, 38.3687, 39.4042, 39.0702, 38.5402, 38.7451, 39.7678, 39.4643, 39.54, 38.5455, 39.292, 39.0653, 40.0644, 39.3368, 39.0566, 39.0194, 40.2326, 39.6897, 40.5741, 39.4724, 39.2891, 39.2251, 39.609, 39.6334, 38.8628, 39.3059, 39.6006, 38.9539, 39.468, 39.1778, 39.3191, 38.5884, 38.684, 39.6718, 38.4444, 39.5037, 39.5587, 39.2563, 39.522, 39.2661, 39.7334, 38.0939, 39.2945, 40.064, 39.0562, 38.6022, 39.7983, 39.626, 40.5086, 39.7061, 39.2236, 38.2181, 39.71, 39.6907, 39.6259, 39.0351, 39.325, 39.4106, 39.9329, 39.5203, 39.2016, 38.2636, 39.8096, 39.8382, 39.5489, 39.1836, 38.6411, 39.718, 39.5925, 39.214, 38.4905, 40.2927, 39.3145, 39.2735, 39.9383, 39.1707, 39.8891, 39.7111, 39.916, 39.3169, 38.1077, 39.3802, 38.9369, 39.0326, 38.1111, 39.8787, 39.7453, 38.9176, 38.9276, 38.7945, 38.9376, 39.7314, 39.1784, 39.3789, 38.5626, 40.0883, 38.5909, 39.6063]

#Collects all the data for quazars together into tuples
allQuasars = list(zip(redShift, bhmass, lum))
#Separates the bals from the regular quazars by taking ones with redshift of over 2.1
bals = [(x, y, z) for (x,y,z) in allQuasars if x > 2.1]

#starting minimum and maximum of the bands of redshift
min = 0
max = 0.4

#creates a dictionary of the bands the quazars that are in the band
dictionary = {}
while(max < 4.9):
    dictionary[np.round((min+max)/2, decimals=1)] = [(x, y, z) for (x,y,z) in allQuasars if min < x and x < max]
    min = max
    max+= 0.1

#separates the means of the bands and the number of quazars in each band into two lists to be plotted against each other
meansofrange = []
lengths = []
for key, lists in dictionary.items():
    meansofrange.append(key)
    lengths.append(len(lists))

#Plots the graph 
plt.plot(meansofrange, lengths,  ls='None', marker='.')
plt.xlabel('avg of redshift band')
plt.ylabel('number Quasars in the band')


#Sorts the masses in descending order
bhmass.sort(reverse=True)
#Get the 50 highest masses of quazars
bhmassclone = bhmass[:50]

upper = []
lower = []
#Classifies the 50 heaviest quazars as upper(BALS) and lower (not BALS)
for mass in bhmassclone:
    for (x, y, z) in allQuasars:
        if(y == mass) and (x > 2.1):
            upper.append((x, y, z))
        elif(y == mass) and (x <= 2.1):
            lower.append((x,y,z))

print(len(upper))
print(len(lower))


#Sorts the luminosity in descending order
lum.sort(reverse=True)
#Gets the 48 highest luminosity quazars
lumclone = lum[:48]

upperlum = []
lowerlum = []

#Classifies the 48 highest luminosity quazars as upper(BALS) and lower (not BALS)
for lumi in lumclone:
    for (x, y, z) in allQuasars:
        if(z == lumi) and (x > 2.1):
            upperlum.append((x, y, z))
        elif(z == lumi) and (x <= 2.1):
            lowerlum.append((x,y,z))

print(len(upperlum))
print(len(lowerlum))