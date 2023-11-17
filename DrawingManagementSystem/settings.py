# ======= REST Framework全局设置 ===========
REST_FRAMEWORK = {
 # ==== 设置全局的Filter_Backends ====
 'DEFAULT_FILTER_BACKENDS': [
    'django_filters.rest_framework.DjangoFilterBackend',
    'rest_framework.filters.SearchFilter',
  ],
  # ===== 设置分页 ===============
 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
 'PAGE_SIZE': 10,
}