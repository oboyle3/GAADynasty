import pandas as pd
from django.core.management.base import BaseCommand
from gaa.models import Player, GAAClub


class Command(BaseCommand):
    help = "Load GAA players from Excel file"

    def handle(self, *args, **kwargs):
        file_path = "irish_players_with_positions.xlsx"

        df = pd.read_excel(file_path)

        created = 0
        skipped = 0

        for _, row in df.iterrows():
            club_name = row["club"].strip()

            club, _ = GAAClub.objects.get_or_create(name=club_name)

            player, created_flag = Player.objects.get_or_create(
                name=row["name"].strip(),
                club=club,
                defaults={
                    "position": row["position"],
                    "overall_rating": int(row["overall_rating"]),
                    "speed": int(row["speed"]),
                    "stamina": int(row["stamina"]),
                    "skill": int(row["skill"]),
                }
            )

            if created_flag:
                created += 1
            else:
                skipped += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Players loaded successfully. Created: {created}, Skipped: {skipped}"
            )
        )
