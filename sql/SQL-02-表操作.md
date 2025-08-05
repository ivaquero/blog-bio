<style>
    table {
        width: auto;
        display: table;
        margin-left: auto;
        margin-right: auto;
    }

    .box {
        display: flex;
    }
    .left {
        width: 200px;
    }
    .right {
        flex: 1;
    }
</style>

# SQL-02-表操作

## 1. 规范

### 1.1. 执行顺序

<div class="box">
    <div class="left">
        1. SELECT <br>
        2. DISTINCT <br>
        3. FROM <br>
        4. JOIN <br>
        5. ON <br>
    </div>
    <div class="right">
        6. WHERE <br>
        7. GROUP BY <br>
        8. HAVING <br>
        9. ORDER BY <br>
        10. LIMIT
    </div>
</div>

### 1.2. 优化原则

- 最大化利用索引；
- 尽可能避免全表扫描；
- 减少无效数据的查询；

## 2. 字段

### 2.1. DISTINCT

```sql
-- 一般情况下，仅使用 DISTINCT 处理单个字段，否则容易引起歧义
-- 多字段不重复查询，使用 GROUP BY
SELECT COUNT(DISTINCT s_id)
FROM student;
```

### 2.2. AS

```sql
-- AS 可以用于创建新列
SELECT title
       ,(domestic_sales + international_sales) / 1000000 AS gross_sales_millions
FROM movies
JOIN boxoffice
ON movies.id = boxoffice.movie_id;
```

## 3. 范围

- 查询条件尽量不用 `<>` 或者 `!=`

### 3.1. WHERE

```sql
-- 全表扫描
SELECT * FROM T WHERE score/10 = 9
-- 走索引
SELECT * FROM T WHERE score = 10*9
```

### 3.2. LIKE

尽量在字段后面使用模糊查询，即 `%` 不出现在字段前。

```sql
-- ale 开头的所有（多个字符串）
SELECT *
FROM [TABLE]
WHERE s_name LIKE 'ale%'
```

```sql
-- ale 开头的所有（一个字符）
SELECT *
FROM [TABLE]
WHERE s_name LIKE 'ale_'
```

```sql
-- 以 "A" 或 "L" 或 "N" 开头
SELECT *
FROM Persons
WHERE City LIKE '[ALN]%'

-- 不以 "A" 或 "L" 或 "N" 开头
SELECT *
FROM Persons
WHERE City LIKE '[!ALN]%'
```

### 3.3. IN / NOT IN

```sql
SELECT name, population
FROM world
WHERE name IN ('Sweden', 'Norway', 'Denmark');
```

尽量避免使用 `IN` 或 `NOT IN`，会导致引擎走全表扫描。对连续值，使用 `BETWEEN`

```sql
SELECT * FROM t WHERE id BETWEEN 2 AND 3;
```

对子查询，可以用 `EXISTS` 或 `NOT EXISTS` 代替

```sql
SELECT *
FROM A
WHERE EXISTS (
SELECT *
FROM B
WHERE B.id = A.id);
```

### 3.4. OR

尽量避免使用 `OR`，会导致数据库引擎放弃索引进行全表扫描，可以用 `UNION` 代替 `OR`。

```sql
SELECT * FROM t WHERE id = 1
   UNION
SELECT * FROM t WHERE id = 3
```

### 3.5. NULL

尽量避免进行 `NULL` 值的判断，会导致数据库引擎放弃索引进行全表扫描。可以给字段添加默认值 0，对 0 值进行判断。

```sql
SELECT * FROM t WHERE score = 0
```

## 4. 排序

### 4.1. ORDER...BY

`ORDER BY` 条件要与 `WHERE` 中条件一致，否则 `ORDER BY` 不会利用索引进行排序。

```sql
-- 不走 age 索引
SELECT * FROM t order by age;
-- 走 age 索引
SELECT * FROM t where age >
 0 order by age;
```

### 4.2. LIMIT

```sql
-- 前 5 行
SELECT * FROM 表 LIMIT 5;
-- 第 4-5 行
SELECT * FROM 表 LIMIT 4, 5;
```

### 4.3. OFFSET

```sql
-- 从第 5 行后的第 5 行
SELECT *
FROM movies
ORDER BY Title ASC
LIMIT 5 OFFSET 5;
```

## 5. 联表操作

### 5.1. JOIN

JOIN 后的 WHERE 用 AND 代替

```sql
-- JOIN = INNER JOIN，无对应关系则不显示
SELECT game.mdate
       ,eteam.teamname
FROM game
JOIN eteam
ON eteam.id = game.team1 AND eteam.coach = 'Fernando Santos'
```

```sql
-- LEFT JOIN：以 A 表为基础查找，若 B 中无对应关系，则值为 null
SELECT A.num
       ,A.name
       ,B.name
FROM A
LEFT JOIN B
ON nid=nid
```

```sql
-- RIGHT JOIN：以 B 表为基础查找，若 A 中无对应关系，则值为 null
SELECT A.num
       ,A.name
       ,B.name
FROM A
RIGHT JOIN B
ON nid=nid
```

```sql
-- FULL JOIN：有对应关系的合并，其余保留，非重复字段不加 TABLE 名区分
SELECT name AS country
       ,code
       ,region
       ,basic_unit
FROM countries
FULL JOIN currencies
ON code=code
WHERE region = 'North America' OR region IS NULL
ORDER BY region;
```

### 5.2. ANTIJOIN

### 5.3. CROSS JOIN

求 Cartesian 积

```sql
-- CROSS JOIN：没有 ON，相当于合并，并混合排序
SELECT c.name AS city
       ,l.name AS language
FROM cities AS c
CROSS JOIN languages AS l
WHERE c.name LIKE 'Hyder%';
```

## 6. 集合操作

### 6.1. UNION

- `UNION` 查询中的每个 `SELECT` 语句必须有相同数量的列
- 若不希望消除重复的行，请使用 `UNION ALL` 而不是 `UNION`

```sql
-- UNION：取并集，重合部分合并
SELECT yr
       ,subject
       ,winner
FROM nobel
WHERE subject = 'physics'
AND yr = 1980 UNION
SELECT yr
       ,subject
       ,winner
FROM nobel
WHERE subject = 'chemistry'
AND yr = 1984
```

### 6.2. UNION ALL

```sql
-- UNION ALL：取并集，不处理重合部分
SELECT nickname
FROM A
UNION ALL
SELECT s_name
FROM B
```

### 6.3. INTERSECT / EXCEPT

- `INTERSECT`：取交集
- `EXCEPT`：取补集

## 7. 分组、聚合

### 7.1. GROUP...BY...

`GROUP BY` 必须在 `WHERE` 之后，`ORDER BY` 之前；

```sql
-- 聚合查询
SELECT num
       ,nid
FROM 表
WHERE nid >
 10
GROUP BY  num
         ,nid
ORDER BY nid DESC
```

### 7.2. HAVING

`GROUP BY` 之后，`ORDER BY` 之前

```sql
-- 包含查询
SELECT num
FROM 表
GROUP BY  num
HAVING MAX(id) >
 10
```

### 7.3. 聚合

- `COUNT(\*)`：计算包含 NULL 和非 NULL 值的行，即：所有行。
- `COUNT(column)`：返回不包含 NULL 值的行数。
- `MIN(column)`, `MAX(column)`
- `AVG(column)`, `SUM(column)`

```sql
SELECT name
       ,CONCAT ( ROUND( 100 * population / (
SELECT population
FROM world
WHERE name = 'Germany' ) ), '%' )
FROM world
WHERE continent = 'Europe'
```

### 7.4. 嵌套聚合

```sql
SELECT countries.name AS country
       ,(
SELECT COUNT(*)
FROM cities
WHERE countries.code = cities.country_code ) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;
```

## 8. 其他函数

### 8.1. 排序

- `DENSE_RANK()`：有 tie 时，tie 为同一位次

```sql
SELECT score
       ,DENSE_RANK() OVER ( ORDER BY score DESC ) AS 'rank'
FROM Scores;
```

## 9. 条件

### 9.1. CASE...WHEN...

```sql
SELECT name
       ,continent
       ,code
       ,surface_area
       ,CASE WHEN surface_area >
        2000000 THEN 'large'
             WHEN surface_area >
              350000 THEN 'medium'  ELSE 'small' END AS geosize_group INTO surface_plus
FROM countries;
WHERE year = 2015;
```

### 9.2. COALESCE

```sql
-- COALESCE takes any number of arguments and returns the first not-null value
SELECT name
       ,party
       ,COALESCE(party,'None') AS aff
FROM msp
WHERE name LIKE 'C%';
```

### 9.3. ALL

```sql
-- 自比较需要限定其范围
SELECT continent
       ,name
       ,area
FROM world x
WHERE area >
= ALL (
SELECT area
FROM world y
WHERE y.continent = x.continent
AND population >
 0 )
```

### 9.4. NULLIF

```sql
-- NULLIF returns NULL if the two arguments are equal
-- otherwise NULLIF returns the first argument
SELECT name
       ,party
       ,NULLIF(party,'Lab') AS aff
FROM msp
WHERE name LIKE 'C%';
```

## 10. 增、改、删

1. 增：`INSERT INTO`
2. 删：`DELETE FROM`
3. 改：`UPDATE...SET`
4. 查：`SELECT...FROM`
5. 备份：`SELECT INTO...(IN...) FROM`

### 10.1. 增加

```sql
INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;
```

```sql
-- 增加数据到指定列
INSERT INTO
  boxoffice (movie_id, rating, sales_in_millions)
VALUES
  (1, 9.9, 283742034 / 1000000);
```

### 10.2. 更新

```sql
Update t1 SET TIME=NOW() WHERE col1=1 AND @now: = NOW();

SELECT @now;
```

## 11. 自定义函数

- 创建：`CREATE FUNCTION [func]([arg1, arg2]) RETURNS [type] BEGIN RETURN ([query]) END`
- 删除：`DROP FUNCTION IF EXISTS [func]`

### 11.1. 创建函数

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN

SET n = n -1; RETURN (

SELECT DISTINCT salary AS NthHighestSalary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET n ); END
```

### 11.2. `:=`

- 用户变量赋值有两种方式：用 `=`，和用 `:=`，其区别在于使用 `set` 命令对用户变量进行赋值时，两种方式都可使用
- 当使用 `SELECT` 语句对用户变量进行赋值时，只能使用 `:=` 方式，因为在 `SELECT` 语句中，`=` 被看作是比较操作符（用于判断，返回 Boolean）
