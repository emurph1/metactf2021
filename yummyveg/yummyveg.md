# Yummy Vegetables
I love me my vegetables, but I can never remember what color they are! I know lots of people have this problem, so I made a site to help.

Here's some sauce to go with the vegetables: index.js

## Solve
Looking at the JS, we see that a query is sent so you can do a UNION attack on this boi.

Make sure you have the same number of columns as the first query though.

To find the number of columns, look at the response after submitting a query (we can just do a empty search).

`UNION SELECT 1, 2, flag FROM the_flag_is_in_here_730387f4b640c398a3d769a39f9cf9b5;--1`

`MetaCTF{sql1t3_m4st3r_0r_just_gu3ss_g0d??}`

