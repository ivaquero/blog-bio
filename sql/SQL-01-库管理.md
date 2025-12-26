# SQL-01-库管理

## 1. 数据库简介

### 1.1. E-R 模型

一个数据库就是一个完整的业务单元，可包含多张表，数据被存储在表中。当前物理的数据库均是按照 E-R 模型（entry-relationship model）进行设计的

1. 一个实体（entry）变换为数据库中的一个表，相当于一个对象
2. 关系用于描述实体间的对应规则，包括一对一、一对多、多对多
3. 关系会变换为数据库表中的一个列
4. 关系型数据库中一行就是一个对象
5. 数据往往会存储在服务器

### 1.2. 三范式

经过研究和对使用中问题的总结，对于设计数据库提出了一些规范，这些规范被称为范式（normal
form，NF）:

1. 第一范式（1NF）：列不可拆分，即关系不可拆分
2. 第二范式（2NF）：唯一标识，可通过一个属性找到其对应的唯一对象
3. 第三范式（3NF）：引用主键，主键即标识；

> 后一个范式均是在前一个范式的基础上建立的。

### 1.3. SQL 语言规范

- SQL 对大小写不敏感
 按惯例，关键字大写，其他小写

## 2. 用户与库

### 2.1. 用户设置

```sql
-- 创建用户
create user '用户名'@'IP 地址' identified by '密码';
-- 删除用户
drop user '用户名'@'IP 地址';
-- 修改用户
rename user '用户名'@'IP 地址'; to '新用户名'@'IP 地址';
-- 修改密码
set password for '用户名'@'IP 地址'=password('新密码')
```

### 2.2. 用户权限设置

```sql
-- 查看权限
show grants for '用户'@'IP 地址'
-- 授权
grant 权限 on 数据库. 表 to '用户'@'IP 地址'
-- 取消权限
revoke 权限 on 数据库. 表 from '用户'@'IP 地址'

-- 备注
- 数据库中的所有数据库名.*
-- 指定数据库中的某张表数据库名。表
-- 指定数据库中的存储过程数据库名。存储过程
-- 所有数据库
.*
-- 用户只能在改 IP 下才能访问用户名@IP 地址
-- 用户只能在改 IP 段下才能访问 (通配符%表示任意) 用户名@192.168.1.%
-- 用户可再任意 IP 下访问 (默认 IP 地址为%) 用户名@%
```

### 2.3. 库的管理

- 创建：CREATE DATABASE \[name\]
 删除：DROP DATABASE \[name\]
 打开：USE \[name\]
 备份
 回复

```sql
CREATE DATABASE school DEFAULT CHARACTER SET = 'utf8mb4';
```

## 3. 数据与键

### 3.1. 键

- 键（key）：值在当前列中具有唯一性
 主键（primary key）：用于惟一确定一个记录的字段，个表中只能含一个主键
- 外键（foreign key）：用于关联两个表
- 有助于确保相关表之间的数据完整性
- 会增大开销
- 超键：在关系中能唯一标识元组的属性集
 候选键：不含有多余属性的超键
 复合键：将多个列作为一个索引键，一般用于复合索引

|      对象       |            定义             |
|:---------------:|:---------------------------:|
| `AUTOINCREMENT` | 字段的值由 SQL 系统负责维护 |
|    `UNIQUE`     |                             |
|   `NOT` NULL    |                             |
|    `DEFAULT`    |                             |
|    `CHECK()`    |                             |

参照完整性要求关系中不允许引用不存在的实体，与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。

### 3.2. 数据类型

- `INTEGER`, `BOOLEAN`
- `FLOAT`, `DOUBLE`, `REAL`
- `CHARACTER()`, `VARCHAR()`, `TEXT`
- `DATE`, `DATETIME`
- `BLOB`

## 4. 表的设计原则

### 4.1. 键

所有的表都有一个主键

- `IDENTITY`: SQL Server, Oracle
- `AutoNumber`: Microsoft Access
- `AUTO_INCREMENT`：MySQL
- `serial`：PostgreSQL

#### 4.1.1. 主键特征

- 名称一般为 id
- INTEGER 型，自动增长
- 值唯一
- 值稳定
- 值非空

> 有些数据库引擎允许空值：如 SQL Server。

### 4.2. 结构

- 尽量不要改变
- 每列只存储一类数据
- 对重要数据，可设置一个 isDelete 的列，类型为 bit 表示逻辑删除

## 5. 表的管理

- 创建：
  - `CREATE TABLE [column] [DataType] [constraint]`
  - `CONSTRAINT [constraint] FOREIGN KEY`
- 修改：
  - `ALTER TABLE`
  - `ADD COLUMN [column] [DataType]`
  - `ADD CONSTRAINT [constraint]`
    - `FOREIGN KEY ([KEY])`
    - `REFERENCES [table] ([KEY])`
  - `DROP`
  - `CHANGE`
  - `RENAME TO [new_table_name]`
- 清空（删除值，但保留结构）
  - `TRUNCATE TABLE table]`
- 删除
  - `DROP TABLE IF EXISTS \[table\]`

### 5.1. 创建

```sql
CREATE TABLE multi_tbl(
  food_id SMALLINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  food_name VARCHAR(20) NOT NULL,
  parent_id SMALLINT UNSIGNED NOT NULL DEFAULT 0
);
```

### 5.2. 修改

```sql
ALTER TABLE mytable ADD COLUMN [column] [DataType] [OptionalTableConstraint] DEFAULT default_value;
```

## 6. 事务

将多个操作被当作一个整体对待。

1. 原子性（Atomicity）：整个事务中的所有操作，要么全部完成，要么全部不完成，不可能停滞在中间某个环节。事务在执行过程中发生错误，会被回滚到事务开始前的状态，就像这个事务从来没有执行过一样
2. 一致性（Consistency）：在事务开始之前和事务结束以后，数据库的完整性约束没有被破坏。
3. 隔离性（Isolation）：隔离状态执行事务，使它们好像是系统在给定时间内执行的唯一操作。这种属性有时称为串行化，为了防止事务操作间的混淆，必须串行化或序列化请求，使得在同一时间仅有一个请求用于同一数据。
4. 持久性（Durability）：事务完成后，该事务所对数据库所作的更改便持久的保存在数据库之中，并不会被回滚。

### 6.1. 功能

1. 当一个业务逻辑需要多个 SQL 完成时，若其中某条 SQL 语句出错，则希望整个操作都退回
2. 使用事务可完成退回的功能，保证业务逻辑的正确性
3. 表的类型必须是 innodb 或 bdb 类型，才可对此表使用事务
4. 主要用于对表进行修改前后的控制

### 6.2. 操作

- `COMMIT`
- `ROLLBACK`
- `SAVEPOINT`
- `SET TRANSECTION`
