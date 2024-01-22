import { Module } from '@nestjs/common';
import { MusicsService } from './musics.service';
import { MusicsController } from './musics.controller';

@Module({
  providers: [MusicsService],
  controllers: [MusicsController]
})
export class MusicsModule {}
