CREATE DATABASE `wiki_sinhala_paragraphs` COLLATE 'utf8mb4_unicode_ci';
use wiki_sinhala_paragraphs;

CREATE TABLE `articles` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `url` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` smallint(5) unsigned DEFAULT NULL,
  `approved` smallint(5) unsigned NOT NULL DEFAULT '2',
  `paragraphs_added` smallint(5) unsigned NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `paragraphs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `article_id` bigint(20) unsigned NOT NULL,
  `paragraph` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `order` smallint(5) unsigned NOT NULL,
  `approved` smallint(5) unsigned NOT NULL DEFAULT '2',
  `no_more_questions` smallint(5) unsigned NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`article_id`) REFERENCES `articles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


ALTER DATABASE wiki_sinhala_paragraphs CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

ALTER TABLE `articles` COLLATE 'utf8mb4_unicode_ci';

ALTER TABLE `paragraphs` COLLATE 'utf8mb4_unicode_ci';

ALTER TABLE paragraphs MODIFY COLUMN paragraph longtext  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL;
ALTER TABLE articles MODIFY COLUMN title mediumtext  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL;
ALTER TABLE articles MODIFY COLUMN url mediumtext  CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL;

-- alter table articles ADD UNIQUE(url(700));

-- CREATE UNIQUE INDEX title_unique_index ON articles (title(600));
-- CREATE INDEX paragraphs_index ON paragraphs (`order`);


-- SELECT id FROM articles ORDER BY id DESC LIMIT 1

-- import
-- docker exec -i db /usr/bin/mysql -uroot --password=pass wiki_sinhala_paragraphs < backup.sql

-- export
-- docker exec docker-tutorial_db_1 /usr/bin/mysqldump -u root --password=root wiki_sinhala_paragraphs > backup.sql

-- mysql -uroot -proot
-- use wiki_sinhala_paragraphs;
-- select count(id),category from articles group by category;
-- select count(id) from articles;


-- to remove duplicate entries
-- DELETE t1 FROM articles t1 JOIN articles t2 ON t2.url = t1.url AND t2.id < t1.id