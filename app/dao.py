from app.models import User
from app import app


# def load_categories():
#     return Category.query.all()
#     # return [{
#     #     'id': 1,
#     #     'name': 'Canon'
#     # }, {
#     #     'id': 2,
#     #     'name': 'Nikon'
#     # }, {
#     #     'id': 3,
#     #     'name': 'Sony'
#     # }]
#
#
# def load_products(kw=None, cate_id=None, page=None):
#     pros = Product.query
#
#     if kw:
#         pros = pros.filter(Product.name.contains(kw))
#
#     if cate_id:
#         pros = pros.filter(Product.category_id.__eq__(cate_id))
#
#     if page:
#         page = int(page)
#         page_size = app.config['PAGE_SIZE']
#         start = (page - 1)*page_size
#
#         return pros.slice(start, start + page_size)
#
#     return pros.all()
#     # pros = [{
#     #     'id': 1,
#     #     'name': 'Canon 750D',
#     #     'price': 7500000,
#     #     'image': 'https://product.hstatic.net/200000354621/product/may-anh-dslr-canon-eos-750d-ef-s18-55-is-stm_40450531012c4f6f89c50efc4fb684de_grande.jpg'
#     # }, {
#     #     'id': 2,
#     #     'name': 'Canon 750D',
#     #     'price': 7500000,
#     #     'image': 'https://product.hstatic.net/200000354621/product/may-anh-dslr-canon-eos-750d-ef-s18-55-is-stm_40450531012c4f6f89c50efc4fb684de_grande.jpg'
#     # }, {
#     #     'id': 3,
#     #     'name': 'Canon 750D',
#     #     'price': 7500000,
#     #     'image': 'https://product.hstatic.net/200000354621/product/may-anh-dslr-canon-eos-750d-ef-s18-55-is-stm_40450531012c4f6f89c50efc4fb684de_grande.jpg'
#     # }, {
#     #     'id': 4,
#     #     'name': 'Sony A6000',
#     #     'price': 10000000,
#     #     'image': 'https://binhminhdigital.com/storedata/images/product/sony-a6000-kit-1650-xam.jpg'
#     # }, {
#     #     'id': 5,
#     #     'name': 'Sony A6000',
#     #     'price': 10000000,
#     #     'image': 'https://binhminhdigital.com/storedata/images/product/sony-a6000-kit-1650-xam.jpg'
#     # }, {
#     #     'id': 6,
#     #     'name': 'Sony A6000',
#     #     'price': 10000000,
#     #     'image': 'https://binhminhdigital.com/storedata/images/product/sony-a6000-kit-1650-xam.jpg'
#     # }]
#     #
#     # if kw:
#     #     pros = [p for p in pros if p['name'].find(kw) >= 0]
#     #
#     # return pros
#
#
# def count_product():
#     return Product.query.count()


def get_user_by_id(user_id):
    return User.query.get(user_id)