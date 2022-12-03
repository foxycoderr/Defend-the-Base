from Source.Scenes.base import BaseScene
import pygame
from Source.settings import Settings
from Source.Objects.monster_base import MonsterBase


class GameScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.path = [[7, 638], [1, 675], [3, 676], [5, 676], [7, 676], [8, 676], [9, 676], [10, 676], [12, 676], [13, 676], [14, 676], [16, 676], [17, 675], [19, 675], [20, 674], [22, 673], [25, 672], [28, 671], [30, 670], [33, 669], [36, 668], [39, 666], [41, 665], [43, 664], [48, 662], [51, 661], [55, 659], [59, 657], [62, 656], [66, 654], [71, 652], [75, 650], [80, 648], [84, 646], [89, 644], [94, 642], [98, 639], [102, 638], [107, 635], [111, 632], [116, 629], [123, 626], [127, 623], [131, 621], [135, 618], [139, 616], [143, 614], [147, 612], [150, 609], [153, 607], [156, 605], [159, 603], [162, 601], [165, 598], [168, 597], [170, 594], [173, 592], [176, 590], [178, 589], [181, 586], [183, 585], [185, 583], [187, 581], [190, 579], [192, 577], [194, 575], [196, 574], [198, 572], [201, 570], [203, 568], [205, 567], [207, 565], [209, 564], [211, 562], [213, 561], [216, 559], [218, 558], [220, 556], [222, 555], [224, 554], [226, 552], [229, 550], [231, 549], [233, 547], [235, 546], [237, 544], [240, 543], [243, 541], [246, 539], [248, 538], [251, 536], [254, 535], [256, 533], [258, 532], [260, 530], [262, 529], [265, 527], [266, 526], [269, 524], [271, 523], [273, 521], [276, 519], [279, 517], [281, 516], [284, 514], [286, 512], [289, 511], [293, 507], [296, 505], [300, 502], [303, 499], [306, 496], [310, 493], [315, 489], [318, 486], [322, 483], [326, 480], [330, 477], [334, 474], [338, 470], [342, 467], [345, 464], [349, 460], [352, 457], [354, 454], [357, 452], [360, 448], [362, 445], [365, 442], [367, 438], [370, 435], [373, 431], [375, 427], [377, 424], [380, 420], [382, 416], [383, 412], [385, 407], [386, 404], [387, 399], [387, 394], [388, 391], [388, 387], [388, 382], [389, 378], [389, 374], [389, 368], [389, 363], [388, 357], [388, 352], [388, 348], [388, 343], [387, 339], [387, 334], [386, 330], [386, 325], [385, 320], [384, 316], [384, 311], [383, 307], [382, 303], [381, 299], [381, 295], [380, 291], [379, 286], [379, 281], [379, 276], [379, 271], [378, 267], [378, 263], [378, 258], [378, 254], [378, 249], [379, 245], [380, 241], [380, 238], [382, 233], [383, 229], [385, 225], [388, 221], [390, 217], [393, 213], [395, 210], [397, 207], [399, 204], [402, 201], [405, 198], [407, 196], [412, 192], [416, 189], [419, 187], [423, 184], [428, 182], [432, 180], [438, 177], [444, 175], [450, 174], [457, 172], [464, 170], [470, 170], [479, 169], [484, 169], [491, 169], [499, 169], [506, 170], [515, 173], [523, 175], [531, 178], [540, 181], [549, 186], [557, 189], [565, 194], [574, 199], [582, 205], [589, 209], [598, 216], [604, 221], [609, 226], [615, 231], [620, 237], [625, 243], [629, 250], [632, 256], [634, 261], [637, 271], [638, 276], [639, 283], [640, 290], [640, 296], [640, 302], [640, 309], [640, 315], [640, 322], [639, 332], [638, 340], [636, 350], [634, 361], [632, 372], [630, 381], [627, 391], [624, 405], [622, 417], [619, 430], [617, 442], [614, 455], [611, 466], [608, 478], [605, 489], [601, 502], [597, 513], [594, 524], [590, 535], [586, 545], [582, 556], [578, 567], [575, 575], [572, 583], [569, 591], [567, 598], [565, 605], [562, 612], [561, 618], [559, 623], [558, 629], [557, 635], [556, 640], [556, 647], [556, 653], [556, 658], [558, 666], [560, 672], [562, 678], [565, 684], [568, 690], [573, 696], [577, 701], [581, 705], [586, 710], [591, 714], [596, 717], [601, 720], [607, 723], [612, 725], [616, 727], [622, 728], [627, 730], [631, 730], [638, 731], [644, 732], [651, 733], [657, 734], [664, 735], [671, 735], [677, 736], [684, 736], [691, 736], [699, 736], [705, 736], [712, 736], [718, 736], [727, 735], [737, 734], [746, 733], [754, 731], [764, 729], [772, 727], [781, 724], [791, 721], [800, 717], [808, 714], [815, 710], [823, 706], [830, 702], [836, 698], [841, 694], [847, 690], [851, 686], [856, 682], [859, 679], [861, 675], [864, 670], [866, 666], [867, 662], [868, 658], [868, 653], [869, 649], [869, 644], [868, 640], [868, 635], [867, 630], [867, 625], [866, 620], [866, 614], [865, 610], [865, 606], [864, 601], [863, 597], [862, 592], [860, 587], [859, 583], [858, 579], [857, 574], [856, 570], [856, 567], [855, 563], [854, 559], [852, 553], [851, 548], [850, 543], [849, 538], [848, 531], [847, 527], [845, 521], [843, 515], [842, 508], [840, 501], [839, 495], [837, 489], [836, 483], [835, 478], [835, 473], [834, 467], [833, 462], [832, 458], [832, 454], [831, 449], [831, 445], [831, 441], [830, 436], [830, 432], [831, 429], [831, 424], [831, 421], [832, 418], [832, 414], [833, 411], [833, 407], [834, 404], [835, 401], [836, 399], [837, 396], [839, 393], [840, 390], [842, 387], [845, 384], [847, 382], [849, 379], [852, 377], [855, 375], [858, 372], [861, 370], [864, 368], [869, 366], [873, 364], [877, 363], [883, 362], [889, 360], [894, 360], [900, 359], [905, 359], [911, 360], [918, 361], [924, 362], [931, 364], [939, 366], [946, 369], [951, 371], [958, 374], [964, 377], [969, 380], [974, 383], [978, 385], [982, 388], [987, 391], [990, 394], [993, 397], [997, 400], [1000, 404], [1002, 408], [1005, 412], [1007, 417], [1009, 422], [1011, 428], [1012, 433], [1013, 439], [1014, 447], [1015, 453], [1015, 460], [1015, 466], [1015, 472], [1015, 480], [1015, 487], [1015, 493], [1014, 500], [1014, 506], [1013, 512], [1012, 519], [1010, 527], [1009, 533], [1008, 540], [1007, 548], [1006, 556], [1005, 563], [1005, 572], [1005, 582], [1005, 589], [1006, 599], [1008, 609], [1009, 618], [1011, 629], [1013, 637], [1016, 646], [1020, 657], [1024, 666], [1029, 675], [1034, 683], [1040, 690], [1045, 697], [1051, 702], [1057, 706], [1063, 709], [1073, 714], [1080, 716], [1089, 717], [1100, 718], [1109, 719], [1120, 718], [1132, 717], [1143, 716], [1155, 715], [1166, 712], [1176, 710], [1186, 707], [1199, 703], [1210, 700], [1219, 696], [1231, 691], [1239, 686], [1246, 681], [1253, 675], [1260, 669], [1265, 664], [1271, 655], [1274, 649], [1277, 643], [1280, 636], [1281, 628], [1283, 621], [1284, 614], [1284, 608], [1285, 600], [1285, 592], [1285, 586], [1285, 579], [1285, 572], [1285, 565], [1285, 558], [1285, 550], [1285, 544], [1284, 538], [1284, 531], [1285, 526], [1286, 518], [1286, 513], [1287, 509], [1288, 504], [1289, 498], [1291, 493], [1292, 489], [1294, 485], [1296, 481], [1298, 477], [1301, 474], [1304, 470], [1307, 468], [1310, 465], [1314, 463], [1319, 460], [1324, 457], [1329, 455], [1334, 453], [1339, 452], [1345, 451], [1351, 450], [1357, 449], [1363, 449], [1369, 449], [1376, 449], [1381, 450], [1388, 451], [1395, 453], [1401, 454], [1406, 456], [1412, 458], [1418, 461], [1423, 463], [1428, 466], [1433, 469], [1437, 471], [1441, 474], [1445, 477], [1449, 479], [1452, 483], [1455, 485], [1458, 488], [1461, 491], [1463, 494], [1465, 497], [1468, 500], [1470, 503], [1472, 506], [1474, 509], [1476, 512], [1478, 515], [1480, 519], [1482, 523], [1484, 526], [1487, 529], [1489, 533], [1491, 536], [1494, 540], [1497, 543], [1499, 546], [1502, 550], [1505, 554], [1508, 557], [1511, 561], [1514, 564], [1517, 567], [1520, 570], [1524, 573], [1529, 576], [1536, 581], [1540, 584], [1545, 586], [1551, 589], [1556, 591], [1561, 593], [1566, 594], [1570, 596], [1574, 597], [1579, 598], [1584, 599], [1588, 600], [1593, 601], [1596, 601], [1600, 601], [1605, 601], [1609, 602], [1613, 602], [1617, 602], [1621, 601], [1624, 601], [1628, 600], [1631, 600], [1634, 599], [1638, 598], [1640, 597], [1641, 597], [1643, 596], [1645, 595], [1646, 595], [1648, 594], [1650, 593], [1651, 592], [1653, 591], [1655, 590], [1656, 589], [1658, 588], [1660, 587], [1662, 586], [1665, 585], [1667, 583], [1669, 582], [1671, 580], [1673, 579], [1675, 577], [1678, 575], [1679, 574], [1681, 572], [1684, 570], [1686, 568], [1688, 565], [1690, 563], [1692, 561], [1694, 557], [1696, 555], [1698, 552], [1700, 549], [1703, 546], [1705, 543], [1707, 540], [1709, 537], [1711, 533], [1713, 530], [1715, 527], [1717, 523], [1719, 520], [1722, 515], [1725, 512], [1729, 508], [1734, 502], [1738, 499], [1743, 495], [1747, 491], [1752, 488], [1756, 484], [1761, 481], [1766, 478], [1772, 475], [1778, 471], [1784, 469], [1789, 467], [1796, 464], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463], [1799, 463]]
        self.monster1 = MonsterBase(self.path)
        self.monster2 = MonsterBase(self.path)
        self.monster3 = MonsterBase(self.path)
        self.progress = [0, 0, 0]
        self.objects.append(self.monster1)
        self.objects.append(self.monster2)
        self.objects.append(self.monster3)



