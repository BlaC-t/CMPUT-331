#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 Zhiyu Li
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
Assignment 9 Problem 3
"""

from sys import flags
from typing import List

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def blockSizeHack(blocks: List[int], n: int, e: int) -> str:
    """
    Hack RSA assuming a block size of 1
    """
    
    # if the block size is one, which means there are only 6 correct keys
    # as long as we much the number in the blocks with the possible keys 
    # generated with symbols than we got the answer
    
    possKeys = []
    for key in range(len(SYMBOLS)):
        possKey = pow(key, e, n)
        possKeys.append(possKey)

    deMsg = ""
    for eachBlock in blocks:
        for eachKey in possKeys:
            if eachBlock == eachKey:
                deMsg += SYMBOLS[possKeys.index(eachKey)]
    
    return deMsg

    

def test():
    "Run tests"
    blocks = [2361958428825, 564784031984, 693733403745, 693733403745,2246930915779, 1969885380643]
    n = 3328101456763
    e = 1827871
    assert blockSizeHack(blocks, n, e) == "Hello."

    blocks = [8217093464028267756409121975787649727933459189613422251056325170128526701608620475172185518043933365298063560742917952159894519863718833263752274042699949617683732661977980412906177305753828819709902244798411894957839707416475280564510910539611544763475123200435434311747842117356528438104670930882089586419285856032456378608099724911919954461399235715511565874538563416970589758277955530087901898217760161217942978391412608505655878814744003765499912581874698703855122674006520835964840975798858622937598839701123281953550868741086184689078242396071897468227558770251846123495197500143759195745133750189771825944450, 7794849320058479483235891570659555002266016547375155834271627867232877707310686790358172752591166222952135096373989699483104805316856153503741983293358686753188375741973694329392994830502219184017253699426225203204479818398602798841738289079920025749304481118864970459430204942049774099091706012023576242951916485698335778583965668014176271693262483148735621817830715145802321491177028501685437330042196652369438353310438870251993388131533357463647258332911941779957582075391493380354231397611607186341163941024721520264506866440403387399875233563475262156689804165564673403583255707102008482769737413240138230958182, 12921037742071842838760612855709802789742552166321664243236891153163955849558252920592898602118263261213407974900684434010883026670588092306944401569637152000644460339661723917340434416156588842120373940380152943221580276004025446469754341544565080637093175331867219444193442557166370387868976245206176371221058518395771129731888292946728299805144265754939474820707438607118730723936438054431075644195757332190639459871665601164359175913274985607634418838742313905513941672317865583833185045818796653788468472146393575895052890874263007974561104147114534063546426622401801687487372757585940996398469423368928561634153, 12921037742071842838760612855709802789742552166321664243236891153163955849558252920592898602118263261213407974900684434010883026670588092306944401569637152000644460339661723917340434416156588842120373940380152943221580276004025446469754341544565080637093175331867219444193442557166370387868976245206176371221058518395771129731888292946728299805144265754939474820707438607118730723936438054431075644195757332190639459871665601164359175913274985607634418838742313905513941672317865583833185045818796653788468472146393575895052890874263007974561104147114534063546426622401801687487372757585940996398469423368928561634153, 11217848754370060151048974509138651367934833846856181914172526865271196973227973032958612071893373870407446424067680428630794833492801574226036772013744651703272011592223995028183588732796708347553596193448469475295048437727499751749496444421871657849036504282377268139817245032192365191518837255326856917027646290383427223544956908427184201140658035239138396681337096013574579279483715854818342002069247473720230879419277515984070934140196174763483942769470443402428741643946856117267859915842392146436529953027444575692012221653374875506494244051455381519411633262533669938622103477152752725216164511652885829931714, 5269654085949312771073284947587463857888800692504926890619354180452852887754690431889392303915723227289884011835096376277337260158302696454089779029540381125567345773162164162213999188043412342585674623646990639766887073454749409214452182338719532431496214971749963450145600078901526394079060905423418009998366490597263514827734649811017719359163561650292798212771095874986931024450160177247698999693852849233711372327005486392709492792111605163663434174292028563844987756427304588985033119954782539430440883646440136433564182087334544672124822547097861537409539709652980649167018619231904494447517171734111089893150]
    n = 14118956157108293655346808051133433894091646039538312006923399735362493605263203702497585893776717003286326229134304078204210728995962809448233282087726441833718356477474042405336332872075207334696535304102256981804931805888502587515310873257966538377740407422137907772437613376342940374815839154897315760145075243071401233858428232725214391295151698044147558454184807105787419519119343953276836694146614061330872356766933442169358208953710231872729486994792595105820069351163066330362191163434473421951082966346860965671789280887020440983279967498480147232734401682910892741619433374703999689201536556462802829353073
    e = 100718103971294791099836725874012546370680926012185805765401052276262582385715159775366446162659948559753647672663811614813769790164114531293175203029620427243719599468958551745636665558941526164523429965489703529940030465646848449715020479155556561228677211251598560502855023412904336022230634725973056990069
    assert blockSizeHack(blocks, n, e) == "Hello."
    
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking

# Invoke test() if called via `python3 a9p1.py`
# but not if `python3 -i a9p1.py` or `from a9p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()