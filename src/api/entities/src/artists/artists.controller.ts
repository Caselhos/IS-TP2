import { Controller, Get, Post, Body, Param, Put, Delete } from '@nestjs/common';
import { ArtistsService } from './artists.service';

@Controller('artists')
export class ArtistsController {
  constructor(private readonly artistsService: ArtistsService) {}

  @Get()
  findAll() {
    return this.artistsService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.artistsService.findOne(id);
  }

  @Post()
  create(@Body() createArtistDto: any) {
    return this.artistsService.create(createArtistDto);
  }

  @Put(':id')
  update(@Param('id') id: string, @Body() updateArtistDto: any) {
    return this.artistsService.update(id, updateArtistDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.artistsService.remove(id);
  }
  @Get(':id/musics')
  getMusics(@Param('id') id: string) {
    return this.artistsService.getMusics(id);
  }
}
