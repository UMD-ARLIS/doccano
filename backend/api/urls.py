from django.urls import include, path

from .views import (comment, example, example_state, health, label, project,
                    tag, task)

urlpatterns_project = [
    path(
        route='category-types',
        view=label.CategoryTypeList.as_view(),
        name='category_types'
    ),
    path(
        route='category-types/<int:label_id>',
        view=label.CategoryTypeDetail.as_view(),
        name='category_type'
    ),
    path(
        route='span-types',
        view=label.SpanTypeList.as_view(),
        name='span_types'
    ),
    path(
        route='span-types/<int:label_id>',
        view=label.SpanTypeDetail.as_view(),
        name='span_type'
    ),
    path(
        route='category-type-upload',
        view=label.CategoryTypeUploadAPI.as_view(),
        name='category_type_upload'
    ),
    path(
        route='span-type-upload',
        view=label.SpanTypeUploadAPI.as_view(),
        name='span_type_upload'
    ),
    path(
        route='examples',
        view=example.ExampleList.as_view(),
        name='example_list'
    ),
    path(
        route='examples/<int:example_id>',
        view=example.ExampleDetail.as_view(),
        name='example_detail'
    ),
    path(
        route='relation_types',
        view=label.RelationTypeList.as_view(),
        name='relation_types_list'
    ),
    path(
        route='relation_type-upload',
        view=label.RelationTypeUploadAPI.as_view(),
        name='relation_type-upload'
    ),
    path(
        route='relation_types/<int:relation_type_id>',
        view=label.RelationTypeDetail.as_view(),
        name='relation_type_detail'
    ),
    path(
        route='tags',
        view=tag.TagList.as_view(),
        name='tag_list'
    ),
    path(
        route='tags/<int:tag_id>',
        view=tag.TagDetail.as_view(),
        name='tag_detail'
    ),
    path(
        route='comments',
        view=comment.CommentList.as_view(),
        name='comment_list'
    ),
    path(
        route='comments/<int:comment_id>',
        view=comment.CommentDetail.as_view(),
        name='comment_detail'
    ),
    path(
      route='examples/<int:example_id>/states',
      view=example_state.ExampleStateList.as_view(),
      name='example_state_list'
    ),
]

urlpatterns = [
    path(
        route='health',
        view=health.Health.as_view(),
        name='health'
    ),
    path(
        route='projects',
        view=project.ProjectList.as_view(),
        name='project_list'
    ),
    path(
        route='tasks/status/<task_id>',
        view=task.TaskStatus.as_view(),
        name='task_status'
    ),
    path(
        route='projects/<int:project_id>',
        view=project.ProjectDetail.as_view(),
        name='project_detail'
    ),
    path('projects/<int:project_id>/', include(urlpatterns_project))
]
