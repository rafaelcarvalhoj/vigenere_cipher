from vigenere_cipher import VigenereCipher

def test_encrypt_known_english_vector():
    assert VigenereCipher.encrypt("HELLO", "KEY") == "RIJVS"


def test_encrypt_preserves_spaces_and_punctuation():
    assert VigenereCipher.encrypt("HELLO, WORLD!", "KEY") == "RIJVS, UYVJN!"


def test_encrypt_identity_with_a_key():
    assert VigenereCipher.encrypt("HELLO", "A") == "HELLO"


def test_encrypt_empty_text_returns_empty():
    assert VigenereCipher.encrypt("", "KEY") == ""


def test_encrypt_portuguese_ascii_case():
    assert VigenereCipher.encrypt("BOM DIA", "CHAVE") == "DVM YMC"


def test_encrypt_normalizes_to_uppercase():
    assert VigenereCipher.encrypt("hello", "key") == "RIJVS"


def test_encrypt_removes_accents_during_normalization():
    assert VigenereCipher.encrypt("maçã", "chave") == "OHCV"
    
def test_big_text_english():
    assert VigenereCipher.encrypt("In a traditional Japanese restaurant in Tokyo, I tried sushi, ramen, and tempura, which were incredibly flavorful. While traveling, I discovered that in Japan it is considered polite to make noise when eating noodles, as this demonstrates appreciation for the meal. In Osaka, I tried takoyaki (octopus balls) and okonomiyaki (a type of Japanese pancake), both of which were considered delicious. The experience was not just about the food, but also about learning the local customs and etiquette. The atmosphere in these smaller, family-owned restaurants often feels more authentic and welcoming than the larger, tourist-focused ones. Trying new foods in a foreign country is definitely one of the best ways to understand a new culture."
                                  ,"water") == "EN T XIWDBXZKNTP AWPTRVOE KIJPANVRJT BR KKKRS, Z PRBIU OULLZ, NAFIE, WNW XVIPNVR, SHBGY SEKI ZJCKIUEBEC WHAOSIBUE. AYELX XIWVXPZJG, B HZOCHZVNEW XYWT BR AWPTR ZP IL GFJSBHVNEW TFHIMI KK MTOV JOBWV SHXR VWTBRX JOHHCAS, TW KDIL HVIOGWKNAMIJ WPIVVYITXZKN YSI PHX QVWL. BR FOADE, Z PRBIU PADSPWKB (STPOIYJ XAEPJ) WNW SBKNHQZUADM (R PYII FB JTTRJELI GWNVEBA), BHXY KF PLZYH PIIA CHRJEDXVVZ DXPZYIHYJ. PHX IOLEKMVJCX ARO NHX AQSM ESKUM XYA FHSU, XUM ECOO TFFQT EIRNNBRX PHX PFYAE GLOTHQJ WNW IKEQNIKPE. MLV WTFSJLHXVV EN MLVOE LQRHLXV, WWMBPP-KWGIU NELXRQRTRKO OYXVJ FXICO MHVV WUMLVJTBG RJD PICYOFMEC TAEE PHX PRNGXV, KKUKMJP-FHGLOEW SEAS. MVPENZ RVS FHSUO IG E WKRXMXJ CHYEPRR MJ ZEYMEETXPP KNX SW PHX FVOT PEPO TH YEZEKWKWNW E EAW VYCPUKI."

def test_big_text_portuguese():
    assert VigenereCipher.encrypt("A biodiversidade, ou diversidade biológica, refere-se à variedade de vida na Terra em todas as suas formas, incluindo a diversidade genética dentro das espécies, a variedade de espécies de plantas, animais, microrganismos e a diversidade de ecossistemas. A preservação da biodiversidade é crucial para o funcionamento dos ecossistemas que sustentam a vida humana, fornecendo serviços essenciais como a polinização de culturas, a purificação da água e do ar, e a regulação do clima. No entanto, a atividade humana, incluindo o desmatamento, a poluição e a urbanização desenfreada, tem levado a uma taxa de extinção de espécies alarmante. A perda de um único elo na cadeia alimentar pode desestabilizar todo um ecossistema. Portanto, a conservação não é apenas uma questão ética, mas uma necessidade para a sobrevivência e o bem-estar das gerações futuras, exigindo ações concretas e sustentáveis em escala global."
                                  ,"loucura") == "L PCQXZVPFMKXRDP, CO FCMECGCFUUE MWINIXINO, LGZVRP-GY C PRRTSXCXV DP JCFU EA ESLTU VM ECXCM RS DIUU ZFRXOM, KHTLFWHFI R DTJYTMZDLRY IYEEEWWC XVNEFI FUJ EDDYECVS, L JUTCVDLRY FY VSASWKYJ DP DFCHKAD, OHKGRID, ACELFRROHKMDOD S U FCMECGCFUUE OS YEIJSTGNGGRS. L DLGMVRGOWCI UA MWIFCMECGCFUUE P QLWWZAW DUTU F FFBWKIEAXSHVI UOD SWQMJIDHYOUJ QFS MWMKEYHUO U MIOO BWGRNL, TITHVCPBXQ MVRGWWQM VSDSHECRID QIOI R PZZCPCQANOI FY TUWHOTUJ, A AILKZZCLQUQ XR ARIU G XF AC, S U TYXUWOWCI UO NZCOU. EO PBNCHKO, L ONKPZDLRY JODAYO, CPWCUTBXQ I UEDAUVUDEYHI, C JFLFWWCI V A FFVCHZZLQUQ XVSPBZTYRDL, HYO FVVLRI C ODA EORC XV EIHCPWRO OS YUJVCTSM CFRRXOHVY. R PPFXC XV UX IHKWF EWC HC WRDPWU CFZMPBNCL GOOS XGMVSEOVKFZZLF NQXF UX SWQMJIDHYOU. GOCHUPNF, A NCHUYIVLQUQ HRO P OJGHRS FAU SOVSEOI GNZCL, AUU ODA YSWGMJIOOXG JRRL O MQVIEGWPGHTIL S I DYD-EDHUT XRS RSLCWFED TOVOIAD, SRKAZNOC UEIVS NCHELVTLG Y UOJTPBNCPVID SG GMTAWO ANISAW."

def test_encrypt_very_long_key():
    text = "ABC"
    key = "LONGKEY"
    assert VigenereCipher.encrypt(text, key) == VigenereCipher.encrypt(text, "LON")