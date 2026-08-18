from django.test import TestCase, Client
from django.urls import reverse
from core.models import Task, Tag


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Tag_1")
        self.task = Task.objects.create(
            content="Test Content", deadline_datetime="2026-08-20"
        )
        self.task.tags.add(self.tag)

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test Content")

    def test_default_is_completed(self):
        self.assertEqual(self.task.is_completed, False)


class TaskViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Tag_1")

        for _ in range(5):
            task = Task.objects.create(
                content=f"Test Content {_}",
                deadline_datetime=f"2026-08-2{_} 1{_}:00:0{_}",
            )
            task.tags.add(self.tag)

        self.client = Client()

    def test_get_list_tasks(self):
        url = reverse("core:task-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tasks"]), 5)

    def test_get_task_detail(self):
        task = Task.objects.filter(pk=2).first()

        url = reverse("core:task-detail", kwargs={"pk": 2})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["task"], task)
        self.assertContains(response, task.content)

    def test_create_task(self):
        url = reverse("core:task-create")
        payload = {
            "content": "New content",
            "deadline_datetime": "2026-08-20 00:00:00",
            "tags": self.tag.pk,
        }

        response_post = self.client.post(url, data=payload)
        self.assertEqual(response_post.status_code, 302)

        url_tasks_list = reverse("core:task-list")
        response = self.client.get(url_tasks_list)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tasks"]), 6)

    def test_update_task(self):
        task = Task.objects.first()

        url = reverse("core:task-update", kwargs={"pk": task.pk})
        payload = {
            "content": "Update content",
            "deadline_datetime": "2026-08-20 00:00:00",
            "is_completed": False,
            "tags": self.tag.pk,
        }

        response_post = self.client.post(url, data=payload)
        task.refresh_from_db()
        self.assertEqual(response_post.status_code, 302)

        url_task_detail = reverse("core:task-detail", kwargs={"pk": task.pk})

        response = self.client.get(url_task_detail)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(task.content, "Update content")
        self.assertEqual(response.context["task"], task)
        self.assertContains(response, "Update content")

    def test_delete_task(self):
        task = Task.objects.first()

        url_delete = reverse("core:task-delete", kwargs={"pk": task.pk})
        response = self.client.post(url_delete)
        self.assertEqual(response.status_code, 302)

        url_tasks_list = reverse("core:task-list")
        response_list = self.client.get(url_tasks_list)
        self.assertEqual(response_list.status_code, 200)
        self.assertEqual(len(response_list.context["tasks"]), 4)

    def test_toggle_complete_button(self):
        task = Task.objects.first()
        self.assertFalse(task.is_completed)

        url = reverse("core:task-toggle", kwargs={"pk": task.pk})

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertTrue(task.is_completed)


class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Tag_1")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Tag_1")


class TagViewTest(TestCase):
    def setUp(self):
        for _ in range(5):
            Tag.objects.create(name=f"Tag_{_}")

        self.client = Client()

    def test_tag_list(self):
        url = reverse("core:tag-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tags"]), 5)

    def test_tag_update(self):
        tag = Tag.objects.first()

        url = reverse("core:tag-update", kwargs={"pk": tag.pk})

        payload = {"name": "New Name"}

        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, 302)

        url_list = reverse("core:tag-list")

        response = self.client.get(url_list)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New Name")

    def test_tag_create(self):

        url = reverse("core:tag-create")

        payload = {"name": "New Created Tag"}

        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, 302)

        url_list = reverse("core:tag-list")

        response = self.client.get(url_list)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tags"]), 6)
        self.assertContains(response, "New Created Tag")

    def test_delete_tag(self):
        tag = Tag.objects.first()

        url = reverse("core:tag-delete", kwargs={"pk": tag.pk})

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

        url_list = reverse("core:tag-list")

        response_list = self.client.get(url_list)

        self.assertEqual(response_list.status_code, 200)
        self.assertEqual(len(response_list.context["tags"]), 4)

    def test_create_tag_invalid_data(self):
        url = reverse("core:tag-create")
        payload = {"name": ""}

        response = self.client.post(url, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tag.objects.count(), 5)
