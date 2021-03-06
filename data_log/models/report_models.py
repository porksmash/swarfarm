from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.db import models

from bestiary.models import Level, GameItem
from data_log.models.log_models import CraftRuneLog, MagicBoxCraft


class Report(models.Model):
    content_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The logging model used to generate this report"
    )
    generated_on = models.DateTimeField(auto_now_add=True)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    log_count = models.IntegerField()
    unique_contributors = models.IntegerField()
    report = JSONField()

    class Meta:
        get_latest_by = 'generated_on'

    def __str__(self):
        return f"{self.generated_on} - {self.content_type}"


class LevelReport(Report):
    level = models.ForeignKey(Level, on_delete=models.PROTECT, related_name='logs')

    def __str__(self):
        return f"{self.level} {self.generated_on}"


class SummonReport(Report):
    item = models.ForeignKey(GameItem, on_delete=models.PROTECT)


class MagicShopRefreshReport(Report):
    pass


class MagicBoxCraftingReport(Report):
    box_type = models.IntegerField(choices=MagicBoxCraft.BOX_CHOICES)


class WishReport(Report):
    pass


class RuneCraftingReport(Report):
    craft_level = models.IntegerField(choices=CraftRuneLog.CRAFT_CHOICES)
