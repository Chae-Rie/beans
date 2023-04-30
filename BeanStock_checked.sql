CREATE TABLE "Fridge" (
  "id" integer PRIMARY KEY,
  "name" varchar(50),
  "location" varchar(50),
  "last_updated" timestamp,
  "is_active" boolean
);

CREATE TABLE "Products" (
  "id" integer PRIMARY KEY,
  "own_article_number" varchar(50),
  "barcode_id" integer,
  "name" varchar(50),
  "category_id" integer,
  "unit" varchar(50),
  "image" bytea,
  "expiry_date" date,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Barcode" (
  "id" integer PRIMARY KEY,
  "barcode" varchar(50),
  "product_id" integer
);

CREATE TABLE "Shoppinglist" (
  "id" integer PRIMARY KEY,
  "name" varchar(50),
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Shoppinglist_products" (
  "id" integer PRIMARY KEY,
  "shoppinglist_id" integer,
  "product_id" integer,
  "quantity" decimal(10),
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "Fridge_products" (
  "id" integer PRIMARY KEY,
  "product_id" integer,
  "fridge_id" integer,
  "unit_id" integer,
  "quantity" integer,
  "barcode_id" integer,
  "added_at" timestamp,
  "expiry_date" date
);

CREATE TABLE "Unit" (
  "id" integer PRIMARY KEY,
  "product_id" integer,
  "unit" varchar(50)
);

CREATE TABLE "Category" (
  "id" integer PRIMARY KEY,
  "name" varchar(50)
);

CREATE TABLE "Ingredient" (
  "id" integer PRIMARY KEY,
  "name" varchar(50),
  "category_id" integer
);

CREATE TABLE "Recipe" (
  "id" integer PRIMARY KEY,
  "name" text,
  "descriptions" text,
  "instructions" text
);

CREATE TABLE "Recipe_ingredient" (
  "id" integer PRIMARY KEY,
  "recipe_id" integer,
  "product_id" integer,
  "unit_id" integer,
  "amount" numeric
);

CREATE TABLE "User" (
  "id" integer PRIMARY KEY,
  "name" varchar(50),
  "email" varchar(50),
  "password" varchar(50),
  "registered_at" date,
  "last_login" timestamp
);

CREATE TABLE "User_recipe" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "recipe_id" integer,
  "added_on" timestamp
);

CREATE TABLE "User_ingredient" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "ingredient_id" integer,
  "quantity" numeric,
  "unit_id" integer,
  "purchase_date" date,
  "expiry_date" date
);

CREATE TABLE "User_shopping_list" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "created_at" timestamp
);

CREATE TABLE "User_shopping_list_item" (
  "id" integer PRIMARY KEY,
  "shoppinglist_id" integer,
  "ingredient_id" integer,
  "quantity" numeric,
  "unit_id" integer
);

CREATE TABLE "Notification" (
  "id" integer PRIMARY KEY,
  "user_id" integer,
  "message" text,
  "created_at" timestamp
);

COMMENT ON COLUMN "Fridge"."location" IS 'z.B.: Küche';

COMMENT ON COLUMN "Fridge"."last_updated" IS 'Zeitpunkt der Änderungen';

COMMENT ON COLUMN "Fridge"."is_active" IS 'Benutzung? Y/N';

COMMENT ON COLUMN "Products"."own_article_number" IS 'für alles wofür es keine EAN gibt';

COMMENT ON COLUMN "Products"."barcode_id" IS 'offizielle nr wenn möglich';

COMMENT ON COLUMN "Products"."unit" IS 'gr, stk, kg...';

COMMENT ON COLUMN "Products"."image" IS 'Zukünftiges Feature für Artikeldarstellung im Dialog';

COMMENT ON COLUMN "Products"."expiry_date" IS 'YYYY/MM/DD';

COMMENT ON COLUMN "Recipe"."name" IS 'Name des Rezepts';

COMMENT ON COLUMN "Recipe"."descriptions" IS 'Beschreibung des Rezepts';

COMMENT ON COLUMN "Recipe"."instructions" IS 'Genaue Beschreibung der Schritte';

COMMENT ON COLUMN "User"."email" IS 'Für Kommunikation';

COMMENT ON COLUMN "User"."password" IS 'verschlüsselt';

COMMENT ON COLUMN "Notification"."message" IS 'Nachricht um den Nutzer hinzuweisen';

ALTER TABLE "Category" ADD FOREIGN KEY ("id") REFERENCES "Products" ("category_id");

ALTER TABLE "Products" ADD FOREIGN KEY ("barcode_id") REFERENCES "Barcode" ("id");

ALTER TABLE "Barcode" ADD FOREIGN KEY ("product_id") REFERENCES "Products" ("id");

ALTER TABLE "Shoppinglist" ADD FOREIGN KEY ("id") REFERENCES "Shoppinglist_products" ("shoppinglist_id");

ALTER TABLE "Products" ADD FOREIGN KEY ("id") REFERENCES "Shoppinglist_products" ("product_id");

ALTER TABLE "Products" ADD FOREIGN KEY ("id") REFERENCES "Fridge_products" ("product_id");

ALTER TABLE "Barcode" ADD FOREIGN KEY ("id") REFERENCES "Fridge_products" ("barcode_id");

ALTER TABLE "Fridge" ADD FOREIGN KEY ("id") REFERENCES "Fridge_products" ("fridge_id");

ALTER TABLE "Unit" ADD FOREIGN KEY ("id") REFERENCES "Fridge_products" ("unit_id");

ALTER TABLE "Products" ADD FOREIGN KEY ("id") REFERENCES "Unit" ("product_id");

ALTER TABLE "Category" ADD FOREIGN KEY ("id") REFERENCES "Ingredient" ("category_id");

ALTER TABLE "Recipe" ADD FOREIGN KEY ("id") REFERENCES "Recipe_ingredient" ("recipe_id");

ALTER TABLE "Products" ADD FOREIGN KEY ("id") REFERENCES "Recipe_ingredient" ("product_id");

ALTER TABLE "Unit" ADD FOREIGN KEY ("id") REFERENCES "Recipe_ingredient" ("unit_id");

ALTER TABLE "User" ADD FOREIGN KEY ("id") REFERENCES "User_recipe" ("user_id");

ALTER TABLE "Recipe" ADD FOREIGN KEY ("id") REFERENCES "User_recipe" ("recipe_id");

ALTER TABLE "User" ADD FOREIGN KEY ("id") REFERENCES "User_ingredient" ("user_id");

ALTER TABLE "Ingredient" ADD FOREIGN KEY ("id") REFERENCES "User_ingredient" ("ingredient_id");

ALTER TABLE "Unit" ADD FOREIGN KEY ("id") REFERENCES "User_ingredient" ("unit_id");

ALTER TABLE "User" ADD FOREIGN KEY ("id") REFERENCES "User_shopping_list" ("user_id");

ALTER TABLE "Shoppinglist" ADD FOREIGN KEY ("id") REFERENCES "User_shopping_list_item" ("shoppinglist_id");

ALTER TABLE "Ingredient" ADD FOREIGN KEY ("id") REFERENCES "User_shopping_list_item" ("ingredient_id");

ALTER TABLE "Unit" ADD FOREIGN KEY ("id") REFERENCES "User_shopping_list_item" ("unit_id");

ALTER TABLE "User" ADD FOREIGN KEY ("id") REFERENCES "Notification" ("user_id");
