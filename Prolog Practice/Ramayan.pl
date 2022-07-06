% Knowledge Base ⬇️
male(ram).
male(lakshman).
male(dashrath).
male(bharat).
male(shatrughna).

female(sita).
female(kaikeyi).
female(sumitra).
female(kaushalya).

parent(dashrath, ram).
parent(dashrath, lakshman).
parent(dashrath, bharat).
parent(dashrath, shatrughna).
parent(kaushalya, ram).
parent(sumitra, lakshman).
parent(kaikeyi, bharat).
parent(kaikeyi, shatrughan).

wife(sita, ram).
wife(kaikeyi, dashrath).
wife(sumitra, dashrath).
wife(kaushalya, dashrath).

% Facts and Rules ⬇️
father(F, S):- male(F), parent(F, S).
father_in_law(F, D):- male(F), parent(F, S), wife(D, S).
mother_in_law(M, D):- female(M), parent(M, S), wife(D, S).
son(F, S):- male(S), parent(F,S).