import { Controller, Get, Post, Body, Param, Put, Delete } from '@nestjs/common';
import { MusicsService } from './musics.service';

@Controller('musics')
export class MusicsController {
  constructor(private readonly musicsService: MusicsService) {}

  @Get()
  findAll() {
    return this.musicsService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.musicsService.findOne(id);
  }

  @Post()
  create(@Body() createMusicDto: any) {
    return this.musicsService.create(createMusicDto);
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateMusicDto: any) {
    return this.musicsService.update(id, updateMusicDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.musicsService.remove(id);
  }
  @Get(':id/artists')
  getArtists(@Param('id') id: string) {
    return this.musicsService.getArtists(id);
  }

  @Get(':id/album')
  getAlbum(@Param('id') id: string) {
    return this.musicsService.getAlbum(id);
  }
}
