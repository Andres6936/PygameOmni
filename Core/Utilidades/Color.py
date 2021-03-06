#!/usr/bin/env python
# coding=utf-8

class Color:

    # DEFINICION DE COLORES

    # ROJOS Y SUS MATICES
    ROJO = (255, 0, 0)
    ROJO_ESPECIFICO = (190, 0, 50)
    ROJO_ESTANDAR = (230, 0, 38)
    ROJO_TOSCANO = (121, 68, 59)
    ROJO_FALUN = (124, 52, 43)
    ROJO_VENECIANO = (110, 67, 60)
    ROJO_MUNSELL = (242, 0, 60)
    ROJO_PERSA = (203, 29, 17)
    ROJO_NCS = (196, 2, 51)
    ROJO_AUTOMOTRIZ = (231, 24, 55)
    ROJO_ANARANJADO = (232, 35, 0)
    ROJO_AURORA = (185, 58, 50)
    ROJO_BANDERA = (173, 21, 25)
    ROJO_CORAL = (229, 29, 46)
    ROJO_INDIO = (165, 67, 50)
    ROJO_DE_FALUN = (165, 67, 50)
    ROJO_FERRARI = (204, 0, 0)
    ROJO_FUCSIA = (255, 0, 90)
    ROJO_SANGRE = (156, 0, 1)
    TOMATE = (213, 48, 62)
    ALMAGRE = (220, 35, 57)
    ALMAGRE_ESPECIFICO = (221, 57, 46)
    RUFO = (203, 109, 81)
    CORAL = (229, 29, 46)
    CARMESI = (220, 20, 60)
    CARMESI_ESPECIFICO = (229, 26, 76)
    BERMEJO = (210, 44, 33)
    BERMELLON = (227, 66, 51)
    BERMELLON_ESTANDAR = (230, 46, 0)
    BERMELLON_DE_CHINA = (178, 26, 39)
    BERMELLON_DE_HOLANDA = (230, 46, 17)
    BORDO = (109, 7, 26)
    VINO = (144, 0, 32)
    ESCARLATA = (255, 36, 0)
    ESCARLATA_ESTANDAR = (253, 45, 28)
    ESCARLATA_ESPECIFICO = (227, 0, 50)
    ESCARLATA_GOBELINOS = (189, 0, 47)
    FRAMBUESA = (230, 29, 82)
    GRANATE = (128, 0, 0)
    GRANATE_ESPECIFICO = (170, 28, 71)
    GRANA = (195, 16, 58)
    CARMIN = (150, 0, 24)
    CARMIN_ESPECIFICO = (229, 26, 76)
    CARMIN_ESTANDAR = (209, 0, 71)
    CARMIN_PICTORICO = (195, 11, 78)
    CARMIN_DE_ALIZARINA = (161, 28, 85)
    AMARANTO = (229, 43, 80)
    HEMATITA_ROJA = (212, 68, 47)
    HIGADO = (137, 30, 53)
    CARDENAL = (196, 30, 58)
    CEREZA = (190, 0, 50)
    GERANIO = (229, 45, 51)
    GULES = (226, 19, 19)
    LACRE_TIPO_UNO = (167, 51, 48)
    LACRE_TIPO_DOS = (193, 36, 34)
    RUBI = (224, 17, 95)
    VINO_TINTO = (130, 0, 0)

    # COLOR ROJO WEB
    CORAL_CLARO = (240, 128, 128)
    ROJO_NARANJA = (250, 69, 0)
    ROJO_LADRILLO = (178, 34, 34)
    BROWN_RED = (165, 42, 42)
    ROJO_OSCURO = (139, 0, 0)

    # COLOR ROJO WEB EN INGLES
    LIGHT_CORAL = (240, 128, 128)
    ORANGE_RED = (250, 69, 0)
    CRIMSON = (220, 20, 60)
    FIRE_BRICK = (178, 34, 34)
    DARK_RED = (139, 0, 0)

    # VERDE Y SUS MATICES
    VERDE = (0, 255, 0)
    VERDE_ESTANDAR = (0, 181, 100)
    VERDE_BRILLANTE = (12, 249, 12)
    VERDE_OSCURO = (34, 139, 34)
    VERDE_OSCURO_WEB = (0, 100, 0)
    VERDE_CLARO_OPACO = (99, 228, 79)
    VERDE_PROFUNDO = (27, 65, 37)
    VERDE_CAZADOR = (53, 94, 59)
    VERDE_BOSQUE = (53, 104, 45)
    VERDE_VERONES = (64, 130, 109)
    VERDE_KELLY = (76, 187, 23)
    VERDE_HELECHO = (113, 188, 120)
    VERDE_MUSGO = (138, 154, 91)
    VERDE_PASTEL = (119, 221, 119)
    VERDE_LORO = (82, 184, 48)
    VERDE_HOJA = (4, 164, 4)
    VERDE_BOTELLA = (0, 106, 78)
    VERDE_MAR = (46, 139, 87)
    VERDE_HOOKER_N1 = (68, 148, 74)
    VERDE_HOOKER_N2 = (59, 120, 97)
    VERDE_PRIMAVERA = (0, 250, 127)
    VERDE_DE_SCHWEINFURT = (0, 155, 125)
    VERDE_DE_PARIS = (18, 131, 133)
    VERDE_OXIDADO = (75, 95, 86)
    VERDE_CENIZA = (95, 127, 122)
    VERDE_GRIS = (67, 179, 174)
    VERDE_PINO = (27, 118, 119)
    SINOPLE = (0, 181, 100)
    PRASINO = (12, 249, 12)
    VIRIDIO = (34, 139, 34)
    CHARTREUSE = (127, 255, 0)
    ESMERALDA = (80, 200, 120)
    ESMERALDA_ESTANDAR = (0, 153, 117)
    ESMERALDA_CLARO = (0, 255, 191)
    XANADU = (155, 134, 120)
    JADE = (0, 168, 107)
    JADE_ESTANDAR = (52, 194, 167)
    ARLEQUIN = (68, 148, 74)
    ESPARRAGO = (123, 142, 35)
    PORRACEO = (27, 65, 37)
    MALAQUITA = (11, 218, 81)
    FORESTA = (53, 104, 45)
    PISTACHO = (147, 197, 114)
    GLAUCO = (113, 188, 120)
    MENTA = (152, 255, 152)
    VERDIN = (119, 221, 119)
    TREBOL = (4, 164, 4)
    OLIVA = (107, 142, 35)
    VERONESE = (24, 168, 141)
    VIRIDIANO = (75, 95, 86)
    VIRIDIANO_ESPANOL = (0, 127, 92)
    VIRIDIANO_INESPECIFICO = (0, 127, 102)
    CARDENILLO = (67, 179, 174)
    TEAL = (27, 118, 119)
    TEAL_OBSCURO = (0, 85, 78)

    # TRANSICION DE AMARILLO A VERDE
    AMARILLO_VERDOSO = (222, 215, 0)
    VERDE_AMARILLO = (198, 206, 0)
    VERDE_AMARILLO_WEB = (173, 255, 47)
    VERDE_AMARILLENTO = (117, 179, 19)
    CHARTREUSE_FRANCES = (223, 255, 0)
    CETRINO_ESPECIFICO = (228, 208, 10)
    LIMA = (158, 253, 78)
    LIMON_ESPECIFICO = (217, 229, 66)
    VERDE_OLIVA = (107, 142, 35)

    # TRANSICION DE VERDE A AZUL
    TURQUESA_ESTANDAR = (93, 193, 185)
    AGUAMARINA_PANTONE = (172, 220, 221)
    VERDE_CIAN = (0, 255, 225)
    VERDE_AZULADO = (13, 152, 186)
    CERCETA = (13, 152, 186)

    # AZUL Y SUS MATICES
    AZUL = (0, 0, 255)
    AZUL_ESTANDAR = (0, 112, 184)
    AZUL_COBALTO = (0, 71, 171)
    AZUL_COBALTO_PICTORICO = (0, 67, 138)
    AZUL_MARINO = (18, 10, 143)
    AZUL_PETROLEO = (1, 70, 99)
    AZUL_FRANCIA = (0, 0, 250)
    AZUL_PRUSIA = (0, 49, 83)
    AZUL_MAJORELLE = (96, 80, 220)
    AZUL_MAJORELLE_ESTANDAR = (85, 100, 235)
    AZUL_KLEIN = (0, 47, 167)
    AZUL_ACERO_CLARO = (176, 196, 22)
    AZUL_GLAUCO = (0, 126, 139)
    AZUL_MARINO_PICTORICO = (10, 63, 122)
    AZUL_MARINO_ESPECIFICO = (67, 110, 192)
    AZUL_CERULEO = (49, 140, 231)
    AZUL_MUNSELL = (0, 147, 175)
    AZUL_ELECTRICO = (44, 117, 255)
    ZAFIRO = (1, 49, 180)
    ZAFIRO_INESPECIFICO = (101, 118, 180)
    INDIGO = (75, 0, 130)
    INDIGO_ESTANDAR = (0, 60, 146)
    INDIGO_PICTORICO = (33, 60, 110)
    TURQUI = (0, 0, 128)
    TURQUI_ESTANDAR = (18, 37, 98)
    AZUR = (0, 153, 255)
    ANIL = (9, 31, 146)
    COBALTO = (51, 60, 135)
    COBALTO_CLARO = (9, 31, 146)
    COBALTO_OBSCURO = (0, 79, 121)
    ORCELA = (37, 32, 111)

    # TRANSICION DE AZUL A PURPURA
    AZUL_PURPUREO = (56, 41, 131)
    AZUL_PURPURA = (76, 40, 130)
    VIOLETA_ESPECIFICO = (76, 40, 130)
    PURPURA_AZULADO = (97, 38, 130)

    # TRANSICION DE PURPURA A ROJO
    PURPURA_ROJIZO = (161, 20, 128)
    ROJO_PURPURA = (228, 0, 120)
    ROJO_PURPUREO = (227, 0, 73)

    # MAGENTA Y SUS MATICES
    MAGENTA_ADITIVO = (255, 0, 255)
    MAGENTA_ESTANDAR = (245, 0, 135)
    MAGENTA_INESPECIFICO = (212, 13, 125)
    FUCSIA = (253, 63, 146)
    FUCSIA_ESPECIFICO = (255, 0, 128)
    FUCSIA_ROJIZO = (255, 0, 90)
    MORADO = (197, 75, 140)
    MALVA = (224, 176, 255)
    LILA = (200, 162, 200)
    SALMON = (254, 195, 172)
    LAVANDA = (230, 230, 250)
    ROSA = (255, 192, 203)
    ROSA_INESPECIFICO = (247, 191, 190)
    ROSA_CORAL = (235, 99, 98)
    ROSA_MEXICANO = (245, 0, 135)
    PIEL = (252, 208, 180)
    ROSADO = (1253, 108, 158)
    ROSADO_PICTORICO = (255, 119, 255)
    ORCEINA = (194, 0, 115)

    # CIAN Y SUS MATICES
    CIAN = (0, 255, 255)
    CIAN_ESTANDAR = (0, 176, 246)
    TURQUESA = (48, 213, 200)
    TURQUESA_ESPECIFICO = (93, 193, 185)
    CELESTE = (135, 206, 255)
    CELESTE_ESTANDAR = (135, 206, 250)
    CELESTE_CLARO = (178, 255, 255)
    CERULEO = (155, 196, 226)
    CERULEO_ESTANDAR = (29, 172, 214)
    CERULEO_INESPECIFICO = (167, 211, 243)
    AGUAMARINA = (127, 255, 212)
    AGUAMARINA_ORIENTAL = (172, 220, 221)
    CALIPSO = (0, 221, 243)
    BIGARO = (204, 204, 255)

    # AMARILLO Y SUS MATICES
    AMARILLO = (255, 255, 0)
    AMARILLO_INDIO = (227, 168, 87)
    AMARILLO_SELECTIVO = (255, 186, 0)
    AMARILLO_LIMON = (255, 248, 59)
    COLZA = (255, 233, 0)
    GUALDO = (255, 215, 0)
    FLAVO = (254, 255, 63)
    AUREO = (253, 253, 150)
    AUREOLINEA = (255, 130, 97)
    LIMON = (253, 232, 15)
    LIMON_ESTANDAR = (217, 229, 66)
    DORADO = (255, 215, 0)
    DORADO_ESPECIFICO = (202, 179, 19)
    DORADO_PICTORICO = (228, 158, 86)
    CADMIN = (255, 246, 0)
    CROMATO = (255, 204, 15)
    ARILADO = (233, 214, 107)
    HANSA = (152, 195, 0)
    ORO = (231, 174, 24)
    AMBAR = (255, 192, 5)
    AMBAR_ESPECIFICO = (250, 215, 0)
    AMBAR_ESTANDAR = (226, 137, 58)
    NAPOLETO = (236, 205, 106)
    NAPOLETO_OSCURO = (255, 201, 77)
    NAPOLETO_CLARO = (255, 246, 173)
    NAPOLETO_ROJIZO = (249, 189, 161)
    CREMA = (255, 240, 201)
    JUNQUILLO = (239, 213, 46)
    MOSTAZA = (232, 191, 6)
    CETRINO = (228, 208, 10)
    CARTUJO = (223, 255, 0)
    GUTA = (228, 115, 15)

    # MARRON Y SUS MATICES
    MARRON = (150, 75, 0)
    MARRON_PICTORICO = (141, 73, 37)
    MARRON_ESPECIFICO = (122, 46, 17)
    MARRON_OSCURO = (119, 53, 37)
    MARRON_SEPIA = (92, 83, 67)
    CAFE_ESPECIFICO = (89, 31, 11)
    PARDO = (105, 76, 65)
    BISTRE = (150, 113, 23)
    ANTE = (186, 124, 69)
    BRONCE = (205, 127, 50)
    MELADO = (209, 149, 56)
    ALMENDRA = (193, 154, 107)
    GAMUZA = (230, 181, 126)
    ARENA = (236, 226, 198)
    CAOBA = (192, 64, 0)
    CAOBA_ESPECIFICO = (165, 102, 93)
    CAOBA_INESPECIFICO = (164, 72, 80)
    CAQUI = (148, 129, 43)
    CAQUI_ESPECIFICO = (224, 216, 176)
    CAQUI_INESPECIFICO = (164, 195, 138)
    CANELA = (153, 107, 66)
    HERRUMBRE = (162, 82, 43)
    LEONADO = (188, 134, 72)
    OCRE = (204, 119, 34)
    OCRE_ESPECIFICO = (185, 147, 90)
    OCRE_AMARILLO = (209, 151, 77)
    OCRE_PICTORICO = (181, 120, 58)
    OCRE_ROJO = (125, 63, 50)
    OCRE_PARDO = (95, 63, 62)
    OCRE_PARDO_OSCURO = (75, 56, 47)
    OCRE_ORO = (87, 63, 37)
    OCRE_DORADO = (201, 126, 40)
    OCRE_DORADO_TOSTADO = (154, 102, 25)
    OCRE_CARNE = (135, 70, 57)
    SECUOYA = (138, 87, 84)
    SEPIA_ESPECIFICO = (102, 59, 42)
    SEPIA_PICTORICO = (82, 75, 59)
    SIENA = (184, 115, 51)
    SIENA_ESPECIFICO = (197, 138, 62)
    SIENA_PALIDO = (218, 138, 95)
    SIENA_TOSTADO = (142, 55, 46)
    TABACO = (80, 48, 30)
    TREVISO = (130, 58, 63)
    WENGUE = (61, 46, 44)
    BORGONA = (128, 0, 32)

    # VIOLETA Y SUS MATICES
    VIOLETA = (139, 0, 255)
    VIOLETA_ESTANDAR = (127, 0, 255)
    LAVANDA_FLORAL = (181, 126, 220)
    AMATISTA = (153, 102, 204)
    AMATISTA_ESPECIFICO = (137, 138, 192)
    PURPURA = (102, 0, 153)
    PURPURA_ESPECIFICO = (125, 33, 129)
    PURPURA_DE_PERKIN = (159, 104, 166)
    PURPURA_DE_TIRO = (102, 2, 60)
    PURPURA_DE_TIRO_ESPECIFICO = (78, 0, 65)
    LIRIO = (127, 105, 165)
    MORADO_INESPECIFICO = (87, 35, 100)
    MORADO_INESPECIFICO_OBSCURO = (74, 35, 100)
    VIOLIN = (161, 6, 132)
    LILA_CLARO = (220, 208, 255)
    LILA_ESPECIFICO = (216, 145, 239)
    LAVANDA_ESPECIFICO = (181, 126, 220)
    ZAFIRO_ESTANDAR = (117, 115, 166)
    ANCIANO = (136, 146, 198)
    UVA = (11, 45, 158)

    # NARANJA Y SUS MATICES
    NARANJA = (255, 112, 40)
    NARANJA_ESPECIFICO = (255, 165, 0)
    NARANJA_OBSCURO = (230, 95, 0)
    NARANJA_CAQUI = (243, 141, 60)
    NARANJA_CAQUI_INESPECIFICO = (226, 95, 35)
    CARA_DE_LUZ = (155, 127, 80)
    ZANAHORIA = (137, 147, 33)
    SESAMO = (255, 140, 105)
    ALBARICOQUE = (251, 206, 177)
    BEIS = (245, 222, 179)
    BEIGE = (232, 225, 158)
    DURAZNO = (255, 200, 160)
    CALABAZA_ESPECIFICO = (237, 170, 124)
    CALABAZA_INESPECIFICO = (217, 147, 67)
    LLAMA = (249, 143, 29)
    SALMON_ESPECIFICO = (250, 128, 114)

    # BLANCOS
    BLANCO = (255, 255, 255)
    BLANCO_ESTANDAR = (250, 250, 250)
    BLANCO_BRILLANTE = (255, 255, 255)
    BLANCO_APAGADO = (246, 246, 246)
    BLANCO_NAVAJO = (235, 225, 201)
    BLANCO_CINC = (250, 251, 253)
    BLANCO_DE_ESPANA = (245, 245, 245)
    BLANCO_AZUL_FRIO = (240, 248, 255)
    BLANCO_MENTA = (245, 255, 240)
    NIEVE = (255, 255, 250)
    NIVEO = (250, 251, 253)
    LINO = (250, 240, 230)
    HUESO = (245, 245, 220)
    MARFIL = (255, 253, 208)
    MARFIL_ESPECIFICO = (245, 242, 231)
    CANDIDO = (255, 255, 255)
    ALBO = (246, 246, 246)
    ALBAYALDE = (245, 245, 245)
    ACELINO = (240, 248, 255)
    LANQUECINO = (245, 255, 240)
    NACAR = (251, 244, 226)
    MADREPERLA = (251, 244, 226)

    # GRISES
    GRIS = (128, 128, 128)
    GRIS_ESTANDAR = (152, 152, 152)
    GRIS_ACORAZADO = (132, 132, 130)
    GRIS_DE_DAVY = (85, 85, 85)
    GRIS_FRIO = (73, 96, 99)
    BISTRE_ESPECIFICO = (128, 117, 90)
    PLATEADO = (192, 192, 192)
    PLATEADO_ESPECIFICO = (205, 205, 205)
    ZINC = (186, 196, 200)
    PLOMO = (192, 192, 192)
    ALUMINIO = (185, 184, 181)
    PLATA = (132, 132, 130)
    PLATA_ANTIGUA = (132, 132, 130)
    SULFAN = (83, 104, 120)
    SULFAN_OSCURO = (54, 69, 79)
    CENIZA = (176, 181, 188)
    LINO_ESPECIFICO = (215, 208, 183)

    # NEGROS
    NEGRO = (0, 0, 0)
    NEGRO_BUJIA = (42, 50, 35)
    NEGRO_DE_HUMO = (56, 34, 18)
    CARBON = (25, 25, 25)
    CORDOBAN = (59, 42, 33)

    # ESMALTES Y METALES HERALDICOS
    GULES_HERALDICO = (237, 28, 36)
    AZUR_HERALDICO = (0, 113, 188)
    SINOPLE_HERALDICO = (0, 143, 76)
    PURPURA_HERALDICO = (99, 11, 87)
    SABLE_HERALDICO = (0, 0, 0)
    ORO_HERALDICO = (234, 193, 2)
    PLATA_HERALDICO = (227, 228, 229)
    ARGEN_HERALDICO = (227, 228, 229)
    MORADO_HERALDICO = (141, 0, 54)
    SANGUINEO = (170, 0, 0)
    LEONADO_HERALDICO = (175, 110, 55)
    NARANJA_HERALDICO = (255, 102, 0)
    CARNACION_HERALDICO = (252, 209, 198)
    CELESTE_HERALDICO = (81, 209, 246)
    CENIZO_HERALDICO = (128, 128, 128)

    # COLORES INSTITUCIONALES Y REGLAMENTARIOS
    ROSSO_CORSA = (204, 0, 0)
    PORTLAND_ORANGE = (255, 90, 54)
    AMBAR_ECE_SAE = (255, 126, 0)
    BRITISH_RACING_GREEN = (0, 66, 37)
    VERDE_AUTOS_FORD = (27, 65, 37)
    AZUL_BRANDEIS = (0, 97, 169)
    AZUL_COLUMBIA = (209, 235, 247)
    AZUL_ETON = (150, 200, 162)
    AZUL_TIFFANY = (129, 216, 208)
    DUKE_BLUE = (0, 26, 87)
    TUFTS_BLUE = (65, 125, 193)
    UCLA_BLUE = (83, 104, 149)

    # COLORES HTML
    TAN = (210, 180, 140)
    WHEAT = (245, 222, 179)
    STEEL_BLUE = (70, 130, 180)
    THISTLE = (216, 191, 216)
    GHOST_WHITE = (248, 248, 255)
    LAVENDER_BLUSH = (255, 240, 245)
    OLD_LACE = (253, 245, 230)
    SEA_SHELL = (255, 245, 238)

    # COLORES FORANEOS
    ALICE_BLUE = (145, 163, 176)
    BEIGE_FORANEO = (245, 245, 220)
    BLEU_DE_DECK = (62, 174, 177)
    BOUGAINVILLEA = (206, 70, 118)
    BUCKSKIN = (151, 127, 115)
    BUFF_TIPO_UNO = (201, 174, 93)
    BUFF_TIPO_DOS = (243, 229, 171)
    BURGUNDY_TIPO_UNO = (103, 49, 71)
    BURGUNDY_TIPO_DOS = (84, 61, 63)
    BURGUNDY_TIPO_TRES = (80, 64, 77)
    GRIS_CADETE_TIPO_UNO = (145, 163, 176)
    GRIS_CADETE_TIPO_DOS = (129, 135, 139)
    CARDINAL = (196, 30, 58)
    FALLOW = (193, 154, 107)
    FUKA_MURASAKI = (86, 57, 112)
    GAMBOGE = (228, 155, 15)
    ICTERINE = (252, 247, 94)
    JASMINE = (248, 222, 126)
    JAUNE_JONQUILLE = (238, 233, 160)
    MOLTEN_LAVA = (184, 41, 40)
    LAVA_TIPO_UNO = (34, 34, 34)
    LAVA_TIPO_DOS = (72, 60, 50)
    LAVA_TIPO_TRES = (59, 49, 33)
    LIVER = (103, 76, 71)
    MURASAKI = (172, 92, 181)
    PERSIAN_ORANGE = (217, 144, 88)
    PINK_ORANGE = (255, 153, 102)
    PORPORA = (178, 27, 28)
    PUMPKIN_TIPO_UNO = (237, 135, 45)
    PUMPKIN_TIPO_DOS = (217, 144, 88)
    PURPLE_TIPO_UNO = (135, 0, 116)
    PURPLE_TIPO_DOS = (96, 47, 107)
    PURPLE_TIPO_TRES = (96, 78, 151)
    SUNSET = (250, 214, 165)
    SPRING_GREEN_UNO = (138, 154, 91)
    SPRING_GREEN_DOS = (147, 197, 146)
    SPRING_GREEN_TRES = (126, 159, 46)
    SPRING_GREEN_CUATRO = (143, 151, 121)
    UPSDELL_RED = (174, 22, 32)
    WINE = (114, 47, 55)

    # OTROS COLORES
    CAFE_CON_LECHE_COSMICO = (255, 248, 231)
    TURQUESA_COSMICO = (156, 255, 206)
    AMARILLO_SIMPSON = (255, 217, 15)